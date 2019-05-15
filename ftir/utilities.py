#!/usr/bin/env python

import spc
import logging
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter


class Spectra:
    
    def __init__(self, spc_file):
        self.spc_file = spc_file
        self.status = 'raw'  # Ideally force people to use a setter for this, but that isn't particularly pythonic
        self.name = self.spc_file
        self.spectra = list()
        self.x_values = list()
        self.read_file()
    
    def read_file(self):
        """
        Reads a raw SPC file, updates the self.spectra attribute to have the raw y values for each index in the spectra
        file
        """
        f = spc.File(self.spc_file) 
        self.spectra = f.sub[0].y
        self.x_values = f.x

    def take_derivative(self, derivative_order):
        # TODO: Make window_length and polyorder user controllable if they end up changing anything
        if derivative_order < 1:
            raise ValueError('Derivative order must be at least 1!')
        if derivative_order > 2:
            logging.warning('Derivatives of order >2 are absolutely not recommended! Use at your own risk.')
        self.spectra = savgol_filter(self.spectra, window_length=5, polyorder=3, deriv=derivative_order)
        self.status += '_deriv{}'.format(derivative_order)
    
    def normalize(self):
        norm = np.linalg.norm(self.spectra)
        for i in range(len(self.spectra)):
            self.spectra[i] = self.spectra[i]/norm
        self.status += '_norm'

    def compare(self, other_spectra, start_coordinate=0, end_coordinate=1000000):
        differences = list()
        if len(self.spectra) != len(other_spectra.spectra):
            raise ValueError('Spectra {} has length {}, and spectra {} has length {}. '
                             'They cannot be compared.'.format(self.name,
                                                               len(self.spectra),
                                                               other_spectra.name,
                                                               len(other_spectra.spectra)))
        if self.status != other_spectra.status:
            logging.warning('Preprocessing done on {} and {} is not the same. Your results probably '
                            'won\'t mean anything!'.format(self.name, other_spectra.name))
        for i in range(len(self.spectra)):
            if start_coordinate <= self.x_values[i] <= end_coordinate:  # Not very efficient, but that shouldn't matter
                differences.append(abs(self.spectra[i] - other_spectra.spectra[i]))
        return np.mean(differences), np.std(differences)

    def plot_spectra(self, output_file=None, clear_figure=True, add_legend=True):
        plt.plot(self.x_values, self.spectra, label=self.name + '_' + self.status)
        if output_file is not None:
            if add_legend is True:
                plt.legend(fontsize='xx-small')
            plt.savefig(output_file)
        if clear_figure is True:
            plt.close()
