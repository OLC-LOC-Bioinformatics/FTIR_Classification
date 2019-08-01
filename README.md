# FTIR Classification

One day, the stuff here will let people classify FTIR spectra of bacteria down to at least genus level,
and hopefully much further than that.

### Installing

To get this installed, clone this repository and run `pip install -e .` from the base of the repository (ideally in some sort
of virtualenv!). To read the spectral (.spc) files that the FTIR machine generates, you need the `spc` module - but not the one
that lives on PyPI. It's available at https://github.com/rohanisaac/spc, so you should be able 
to install it with a `pip install git+https://github.com/rohanisaac/spc.git`. 

### Usage

Currently, this only really provides a class that can help with some common FTIR spectral file
manipulations. Here's an example of what you can do:

```python
# Load in our cool spectra class!
from ftir.utilities import Spectra

# Read in some spectral files
spectra_one = Spectra('path/to/spectra_one.spc')
spectra_two = Spectra('path/to/spectra_two.spc')

# Do some pre-processing on both - take a first derivative and do vector normalization
# Also subset to only take x-values between 900 and 1400
spectra_one.take_derivative(1).normalize().subset_spectra(900, 1400)
spectra_two.take_derivative(1).normalize().subset_spectra(900, 1400)

# You can access the y-values for each spectra with .spectra attribute, which is a list
yvals = spectra_one.spectra

# Compare two spectra to see what the mean and stdev of differences at each point is
avg_diff, stdev_diff = spectra_one.compare(spectra_two)

# Plot the spectra for visual inspection
spectra_one.plot_spectra(clear_figure=False)
spectra_two.plot_spectra(output_file='spectral_plot.png')
```