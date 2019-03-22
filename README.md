# FTIR Classification

One day, the stuff here will let people classify FTIR spectra of bacteria down to at least genus level,
and hopefully much further than that.

### Installing

To read the spectral (.spc) files that the FTIR machine generates, you need the `spc` module - but not the one
that lives on PyPI. It's available at https://github.com/rohanisaac/spc, so you should be able 
to install it with a `pip install git+https://github.com/rohanisaac/spc.git`. 

Everything else should get installed automatically when you `pip install ftir_classify` (once I actually 
put this on PyPI).