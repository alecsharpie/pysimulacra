

# Dataset

download dataset and get info here:
https://github.com/JD-P/simulacra-aesthetic-captions

# Install

Clone the project and install it:

```bash
git clone git@github.com:alecsharpie/pysimulacra.git
cd pysimulacra
make install # or `pip install .`
```

# Example

Download the data from the repository linked above and instantiate the class pointing to the sql db. Do it manually (eg with chrome) if curl isn't working


```python
from pysimulacra.data import SimulacraData

ds = SimulacraData('/data/sac_public_2022_06_29.sqlite')

data = ds.fetch_all_data()
```
here `data` is a dictionary containing all tables from db, key = table_name, value = pd.DataFrame tables.

```
Table : col1, col2, col3, ...
----------
survey  :  id, qid, rating
generations  :  id, sid, method, prompt, verified
images  :  id, gid, idx
paths  :  iid, path
ratings  :  sid, iid, rating, verified
upscales  :  iid, method
```

```
ds.get_image_paths_and_prompts()

ds.get_prompts_and_ratings()

ds.get_image_paths_and_prompts_and_ratings()
```
