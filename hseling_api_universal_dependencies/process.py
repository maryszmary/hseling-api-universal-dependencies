from hseling_api_universal_dependencies.conllu_graphs import get_multi_sentence, get_combined


def process_data(contents, pipeline):
    """
    Process the contents of the file, which is always one sentence.
    """
    if isinstance(contents, bytes):
        text = contents.decode('utf-8')
    else:
        text = contents
    sentence = text.strip()
    parsed = pipeline.process(sentence)
    return parsed
