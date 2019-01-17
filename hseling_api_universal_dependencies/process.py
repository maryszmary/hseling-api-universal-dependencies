from hseling_api_universal_dependencies.conllu_graphs import get_multi_sentence, get_combined
from hseling_api_universal_dependencies.examples import hardcoded


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
    # ms = get_multi_sentence([sentence, parsed])
    # ms = get_multi_sentence([sentence, hardcoded])
    # mst = get_combined([ms])
    # return mst[0]
    return parsed