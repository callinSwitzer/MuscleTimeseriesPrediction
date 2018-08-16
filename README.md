# MuscleTimeseriesPrediction
Predict muscle length from EMG data



1. Clone this repository

2. Navigate to the directory of this repo

If you want to use tensorflow with cpu

```
conda env create environment_cpu.yml
```

GPU version:

```
conda env create environment.yml
```
3. Activate the new environment 

```
activate timeseries_learn
```

on mac
```
source activate timeseries_learn
```

4. Install kernel, so you can select in jupyter lab/notebook

```
python -m ipykernel install --user --name timeseries_learn
```
5. deactivate conda environment
```
deactivate
```
on mac
```
source deactivate
```
