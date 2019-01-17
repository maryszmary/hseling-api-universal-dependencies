from ufal.udpipe import Model, Pipeline

MODELS_DIR = '/dependencies/hseling_api_universal_dependencies/models/'
MODEL_NAMES = {
	'russian': 'russian-ud-2.0-170801.udpipe'
}

def load_model(language):
	model = Model.load(MODELS_DIR + MODEL_NAMES[language])
	pipeline = Pipeline(model, '', '', '', '')
	return pipeline