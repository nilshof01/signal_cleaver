# signal_cleaver
## Installation 

1. You have to get the licence, download and dezip the package from https://services.healthtech.dtu.dk/service.php?SignalP-6.0 
2. After you have deziped the package you open a conda environment (I used python 3.7) in your IDE.
```python
conda create -n myenv python=3.7
conda activate myenv
```
3. Then you install torch>1.7.0
```python
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=10.2 -c pytorch
```
4. After that you have to copy the model weights (.pt ending) from the signalp-6-package/models to signalp-6-package/signalp/model_weights (Just do a drag and drop)
5. Then type in your terminal pip install signalp-6-package/
6. Finally type in the terminal pip install requirements.txt

## Run
To run the the script you have to go to signal_cleaver_2 and scroll down to "main" and press play.
