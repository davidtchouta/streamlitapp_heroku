MLOPS Tutorials :


Deploy ML flask App in : 
	- AWS Fargate ===>  Tutorial already done ✅
	- GCP ===> Tutorial already done ✅
	- Azure Cloud ===> Tutorial already done ✅


Build, train and deploy models in AWS Sagemaker ===> Tutorial already done ✅

Build Gradio app and deploy in Hugging Face Tutorial already done ✅



Build Streamlit app and deploy in Render hosting solution ===> covered today 🏃🏃🏃🏃


ML Pipelines :
	- ZenML
	- MLFlow
	- KubeFlow
	- DVC
	- Pycaret




# Build Streamlit app and deploy in Render hosting solution

	conda create -n streamlitenv python=3.8
	conda activate streamlitenv
	pip install pycaret
	pip install ipykernel
	python -m ipykernel install --user --name pycaretenv --display-name "pycaretenvkernel"
	lancer jupyter depuis batch
	jupyter notebook

Got to the https://dashboard.render.com/
logging with your github
set the github repository

See your streamlit app in action : https://streamlit-ml-deplyment.onrender.com
