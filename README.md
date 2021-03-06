# Dirac interfaced with Openfermion

# Requirements

- Dirac 
- Openfermion
- all requirements for the aforementioned programs.

# Installation

INSTALL DIRAC: http://diracprogram.org/doku.php

Note that one should modify the parameter variables in ```/path/to/dirac/utils/dirac_mointegral_export.F90``` before compiling,
such that

```
  logical, parameter     :: generate_full_list = .true.
  logical, parameter     :: generate_lower_triangular = .false.
  logical, parameter     :: sorting_wrt_energy = .true. ! sort wrt spinor's energy.
  logical, parameter     :: sorting_wrt_occupied = .false. ! sort wrt spinor's lowest occupied
```

INSTALL OPENFERMION : https://github.com/quantumlib/OpenFermion

INSTALL Openfermion-Dirac interface:

Clone the complete repository:
```
$ git clone https://github.com/bsenjean/Openfermion-Dirac.git
```

Build the code:
```
$ cd /path/to/Openfermion-Dirac/
$ pip install -e .
```

In ```/path/to/Openfermion-Dirac/openfermion_dirac/_run_dirac.py``` change the following :
- Set your own path to ```pam``` (```pam``` is the run_script of the Dirac program), which is called in the subprocess,
or set ```/path/to/dirac/build``` to your ```.bash_profile```.
- Same for ```dirac_mointegral_export.x```.
- I realized that the last release of DIRAC may not have the complete version of ```dirac_mointegral_export.x```. One might need to use ```dirac_openfermion_mointegral_export.x``` instead (which do not exist anymore in the developer version as it has been merged with ```dirac_mointegral_export.x```). To make everything working (like the calculation of property integrals), please change ```dirac_mointegral_export.x``` to ```dirac_openfermion_mointegral_export.x``` in ```/path/to/Openfermion-Dirac/openfermion_dirac/_run_dirac.py```.

# Use

Different examples are furnished in the examples/ repository in python, as well as a tutorial in tutorial/. If one wants to play more with the tutorial, use jupyter notebook to do so.
