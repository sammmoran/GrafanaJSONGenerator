
import argparse


def main(files):

    




if __name__=="__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file',nargs='+',help='path to the file')

    #Parse the files separately
    args_namespace=parser.parse_args()
    args=vars(args_namespace)['file']
    main(args)
