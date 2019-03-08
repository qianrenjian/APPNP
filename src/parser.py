import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it trains on the Cora dataset.
    The default hyperparameters give a good quality representation without grid search.
    """

    parser = argparse.ArgumentParser(description = "Run PPNP/APPNP.")

    parser.add_argument("--edge-path",
                        nargs = "?",
                        default = "./input/cora_edges.csv",
	                help = "Edge list csv.")

    parser.add_argument("--features-path",
                        nargs = "?",
                        default = "./input/cora_features.json",
	                help = "Features json.")

    parser.add_argument("--target-path",
                        nargs = "?",
                        default = "./input/cora_target.csv",
	                help = "Target classes csv.")

    parser.add_argument("--model",
                        nargs = "?",
                        default = "exact",
	                help = "Model type.")

    parser.add_argument("--epochs",
                        type = int,
                        default = 1000,
	                help = "Number of training epochs. Default is 1000.")

    parser.add_argument("--seed",
                        type = int,
                        default = 42,
	                help = "Random seed for train-test split. Default is 42.")

    parser.add_argument("--iterations",
                        type = int,
                        default = 10,
	                help = "Number of Approximate Personalized PageRank iterations. Default is 10.")

    parser.add_argument("--training-size",
                        type = int,
                        default = 1500,
	                help = "Training set size. Default is 1500.")

    parser.add_argument("--batch-size",
                        type = int,
                        default = 128,
	                help = "Batch size. Default is 128.")

    parser.add_argument("--dropout",
                        type = float,
                        default = 0.5,
	                help = "Dropout parameter. Default is 0.5.")

    parser.add_argument("--alpha",
                        type = float,
                        default = 0.1,
	                help = "Page rank teleport parameter. Default is 0.7.")

    parser.add_argument("--learning-rate",
                        type = float,
                        default = 0.001,
	                help = "Learning rate. Default is 0.01.")

    parser.add_argument("--lambd",
                        type = float,
                        default = 0.001,
	                help = "Weight matrix regularization. Default is 0.005.")

    parser.add_argument("--layers",
                        nargs="+",
                        type=int,
                        help = "Layer dimensions separated by space. E.g. 64 64.")

    parser.set_defaults(layers = [64, 64])
    
    return parser.parse_args()
