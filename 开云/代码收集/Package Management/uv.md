# Macos install uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
# or
wget -qO- https://astral.sh/uv/install.sh | sh
# or specify version
curl -LsSf https://astral.sh/uv/0.9.27/install.sh | sh
# or using pipx to install
pipx install uv
# or
pip install uv
# or
brew install uv
```
# Check if uv is installed
```
uv --version
uv
```
# Create a virtual environment and activate it
```
# simple create a env
uv venv
# choose a folder to create env
uv venv my-name
# specify a python version
uv venv --python 3.11
# using source .venv/bin/activate to activate the env
# use deactivate to deactivate the env
```
# Install/uninstall a package in the virtual environment
```
uv pip install xxx
uv pip uninstall
```
#  Run a script
```
uv run
```