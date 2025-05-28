import logging

logging.basicConfig(level=logging.DEBUG)

from hta.trace_analysis import TraceAnalysis
from hta.common.trace_parser import (
    _auto_detect_parser_backend,
    get_default_trace_parsing_backend,
    ParserBackend,
    set_default_trace_parsing_backend,
)

def main():
    # set_default_trace_parsing_backend(ParserBackend.IJSON_BATCH_AND_COMPRESS)
    analyzer = TraceAnalysis(
        trace_dir="test-trace",
    )
    overlap_df = analyzer.get_comm_comp_overlap(visualize=True)

if __name__ == "__main__":
    main()
