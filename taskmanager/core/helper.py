from datetime import datetime
import pytz


def get_epoch_timestamp(date):
    """
    Return epoch timestamp in miliseconds if given date
    :param date:
    :return:
    """
    epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.UTC)
    return int((date - epoch).total_seconds() * 1000.0)