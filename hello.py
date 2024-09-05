import argparse

parser = argparse.ArguementParser(
    description='Provides a personal greeting.'
)

parser.add_argument(
    "-n,""--name",metavar="name", dest="firstname"
    required=True, help= "The name of the person to greet."
)

args =parser.parse_args()

msg = f"Hello{args.name}!"
print(msg)
