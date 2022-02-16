## cef2isotope

This repository contains a python scirpt to parse metabolomics cef file to csv file containing list of isotopes.

The command line to launch is :
```bash
python3 export_isotopes <path_to_cef_file>
```

The output will be a csv file like the one following :

|   compoundID   | parentMZ | parentRT | adduct |     x    |    rx    |     y    |  z  |
|:--------------:|:--------:|:--------:|:------:|:--------:|:--------:|:--------:|:---:|
| 188.0395@0.518 | 188.0395 | 0.518    | M+H    | 189.0468 | 189.0469 | 18727.65 | 1   |
| 188.0395@0.518 | 188.0395 | 0.518    | M+H+1  | 190.0479 | 190.0472 | 3247.60  | 1   |
| 139.9523@0.518 | 139.9523 | 0.518    | M+H    | 140.9593 | 140.9610 | 19188.86 | 1   |
| ...            | ...      | ...      | ...    | ...      | ...      | ...      | ... |
