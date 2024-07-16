# cupy-exploration

Testing <strike>cuDF</strike> - make that cupy - for disease modeling.

- [cuDF](https://docs.rapids.ai/api/cudf/stable/)
  - [GitHub](https://github.com/rapidsai/cudf)
  - use `nvidia-smi` to determine which version of CUDA (if any!) you have installed[\*](#nvidia-smi)
  - ```pip install --extra-index-url=https://pypi.nvidia.com cudf-cu11```
  - ```pip install --extra-index-url=https://pypi.nvidia.com cudf-cu12```
- [cupy](https://docs.cupy.dev/en/stable/index.html)
  - use `nvidia-smi` to determine which version of CUDA (if any!) you have installed[\*](#nvidia-smi)
  - ```pip install cupy-cuda11x```
  - ```pip install cupy-cuda12x```

## queuepy.ipynb

- [SEIR with cupy](cuseir.ipynb)

### `nvidia-smi`

```
$ nvidia-smi
Tue Jul 16 22:47:27 2024       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.161.08             Driver Version: 535.161.08   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A40-4Q                  On  | 00000000:03:00.0 Off |                    0 |
| N/A   N/A    P8              N/A /  N/A |      0MiB /  4096MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
```
