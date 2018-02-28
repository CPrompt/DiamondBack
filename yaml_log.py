#!/usr/bin/python
import logging
import logging.config


def configure_logger(name, log_path):
    logging.config.dictConfig({
        'version':1,
        'formatters':{
            'default':{'format': '%(asctime)s - %(levelname)s - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'}
            },
        'handlers':{
            'file':{
                'level':'DEBUG',
                'class':'logging.handlers.RotatingFileHandler',
                'formatter':'default',
                'filename': log_path,
                'maxBytes':1024,
                'backupCount':2
                }
            },
        'loggers':{
            'default':{
                'level':'DEBUG',
                'handlers':['file'],
                }
            },
        'disable_existing_loggers': False
        })
    return logging.getLogger(name)
