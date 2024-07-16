from timeit import timeit

import cudf as cd
import numpy as np
import pandas as pd

COUNT = 1_000_000
PREVALENCE = 0.10
NUM_NODES = 768

CUDF = True

infectious = (np.random.random(COUNT) < PREVALENCE).astype(np.uint8)
itimer = np.zeros(COUNT, dtype=np.uint8)
itimer[infectious != 0] = np.random.randint(1, 8, infectious.sum())
nodeid = np.random.randint(0, NUM_NODES, COUNT)

cudf = cd.DataFrame({"nodeid": nodeid, "infectious": infectious, "itimer": itimer})
pddf = pd.DataFrame({"nodeid": nodeid, "infectious": infectious, "itimer": itimer})

REPS = 100
elapsed = timeit(
    "pddf.groupby('nodeid')['infectious'].sum()", globals=globals(), number=REPS
)
print(
    f"Elapsed time (Pandas): {elapsed:.4f} seconds ({round(REPS*COUNT/elapsed):13,} rows/s)"
)
elapsed = timeit(
    "cudf.groupby('nodeid')['infectious'].sum()", globals=globals(), number=REPS
)
print(
    f"Elapsed time (cuDF):   {elapsed:.4f} seconds ({round(REPS*COUNT/elapsed):13,} rows/s)"
)

print("CUDF: ")
print(cudf.groupby("nodeid")["infectious"].sum().sort_index())
print()
print("PANDAS: ")
print(pddf.groupby("nodeid")["infectious"].sum())

...
