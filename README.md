# Create your enviroment using anaconda 
```bash
$ conda create --name odoo
 
```
# Activate the env 
```
$ conda activate odoo
```

### Run the fastApi server 
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```