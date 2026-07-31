# Setup Instructions

## 1. Install SynthStrip

First, verify whether `nipreps-synthstrip` is already installed.

```bash
which nipreps-synthstrip
```

If it is not installed, install it using:

```bash
pip install nipreps-synthstrip
```

Verify the installation:

```bash
which nipreps-synthstrip
```

### Download the SynthStrip Checkpoint

Download the pre-trained SynthStrip model (`synthstrip.pt`) from the official SynthStrip documentation:

[SynthStrip Checkpoint Download](https://surfer.nmr.mgh.harvard.edu/docs/synthstrip/?utm_source=chatgpt.com)

Place the downloaded `synthstrip.pt` file in your preferred directory (for example, `synthstrip/synthstrip.pt`) and update its path in `config.py`.

---

## 2. Install ANTs

ANTs is required for image registration.

### Download ANTs

```bash
cd ~

wget https://github.com/ANTsX/ANTs/releases/download/v2.5.4/ants-2.5.4-ubuntu-22.04-X64-gcc.zip
```

### Extract the package

```bash
unzip ants-2.5.4-ubuntu-22.04-X64-gcc.zip
```

### Configure environment variables

```bash
echo 'export ANTSPATH=$HOME/ants-2.5.4/bin/' >> ~/.bashrc
echo 'export PATH=$ANTSPATH:$PATH' >> ~/.bashrc

source ~/.bashrc
```

### Verify the installation

```bash
which antsRegistration
which antsRegistrationSyNQuick.sh
```

Both commands should return the corresponding executable paths.

### Update ANTs Path

Open `config.py` and update the `ants_bin` variable to point to the ANTs `bin` directory. For example:

```python
ants_bin = "/home/<username>/ants-2.5.4/bin"
```

---

## 3. Update Configuration

Open `config.py` and update the following paths according to your local setup:

* `ants_bin`
* Template directory path 

Example:

```python
ants_bin = "/home/<username>/ants-2.5.4/bin"

TEMPLATE_PATH = "/path/to/template"
```

Replace the placeholder paths with the actual locations on your machine before running the application.
