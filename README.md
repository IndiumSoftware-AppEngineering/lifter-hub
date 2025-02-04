# lifter-hub

# Build
```
pip install -r requirements.txt
```

```
python setup.py sdist bdist_wheel
```

# install from filesystem
```
pip install path/to/lifter-hub
```

# install from github
```
pip install git+https://github.com/IndiumSoftware-AppEngineering/lifter-hub.git

```

# Usage

```
from lifter import hub

# Initialize database (Choose "sqlite" or "postgres")
prompt_hub = hub.init(db_type="sqlite")  # or "postgres"

# Create a prompt
prompt_hub.create("greeting", "Hello, world!")

# Retrieve a prompt
prompt = prompt_hub.pull("greeting")
print("Fetched prompt:", prompt)

# Update a prompt
prompt_hub.update("greeting", "Hello, Python!")

# Delete a prompt
prompt_hub.delete("greeting")
```