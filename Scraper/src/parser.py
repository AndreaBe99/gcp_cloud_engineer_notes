import argparse


def prepare_parser():
    parser = argparse.ArgumentParser(
        description="Generate PDFs for GCP ACE exam questions"
    )
    parser.add_argument(
        "--start", default=1, type=int, help="First question index to query"
    )
    parser.add_argument(
        "--end", default=190, type=int, help="Last question index to query"
    )
    parser.add_argument(
        "--pages",
        default=[3, 4, 5],
        type=int,
        nargs="+",
        help="Specify pages to generate",
    )
    parser.add_argument(
        "--exam", default="gcp-ace", choices=["gcp-ace", "aws-scs"], help="Exam name"
    )
    parser.add_argument(
        "--test", action="store_true", help="Use local HTML files for testing"
    )
    return parser
