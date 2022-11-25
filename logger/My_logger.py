import logging
import os

default_dir_logs = os.path.join(os.path.dirname(__file__), 'logs')


def get_logger(name_log):
    final_path = os.path.join(default_dir_logs, name_log)
    logging.basicConfig(filename=final_path,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    return logging


if __name__ == '__main__':
    l = get_logger("jeje.txt")
    l.info("jiji")
