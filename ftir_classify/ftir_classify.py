#!/usr/bin/env python

import spc
import keras
import numpy as np


def main():
    """
    Figure out if an isolate is priority serotype of Salmonella or something else entirely.

    This function will (preliminarily) do the following:
    1a) Read in an FTIR spectra and take its first derivative and normalize it.
    1b) Implement a check to make sure that a sample is dried out/otherwise terrible quality
    2) Figure out if sample is gram positive or negative. If positive stop. If negative, proceed.
    3) Figure out if sample is salmonella or other. If other, stop. If salmonella, proceed.
    4) We care about 6 Salmonella serotypes: Enteritidis, Typhimurium, Heidelberg, Newport, Thompson, and Hadar.
    Seems to be very difficult, bordering on impossible, to do a 7-way classification where we actually find
    out if a sample is one of our 6 important serotypes or something else, likely because our training data is pretty
    small. What does seem to work fairly well is doing a one-vs-all for each serotype. We can predict fairly
    accurately (with slight overprediction)  if something is one serotype or not (so check each serotype individually)

    Important to note that false positives are OK, but false negatives are REALLY REALLY BAD.
    """

    print('Hello')


def read_spectra(spectral_file, start_x=600, end_x=1450):
    """
    Uses spc module from https://github.com/rohanisaac/spc (which appears to be abandonware, but has yet to fail on me)
    to read in a spectral file, then takes its first derivative and normalizes its data.
    :param spectral_file: A .spc file produced by our super duper FTIR machine.
    :param start_x: Start of interval over which we want to look at data
    :param end_x: End of interval over which we want to look at data
    :return: Normalized first derivative over the interval specified.
    """
    assert end_x > start_x
    spectral_data = spc.File(spectral_file)
    y = list()
    # Iterate through file, taking first derivative over our range of important stuff.
    for i in range(len(spectral_data.x) - 2, 0, -1):
        x_value = spectral_data.x[i]
        if start_x < x_value < end_x:
            difference = spectral_data.sub[0].y[i] - spectral_data.sub[0].y[i + 1]
            y.append(difference)
    # Note: it's possible to get a value of zero for norm if the array has all 0 values - this seems really (x1000000)
    # unlikely to ever happen with a spectra, so we won't bother catching an error here.
    norm = np.linalg.norm(y)
    return y/norm


if __name__ == '__main__':
    main()
