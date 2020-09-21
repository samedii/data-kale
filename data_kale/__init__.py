from data_kale.download import download
from data_kale.upload import upload
from data_kale.path import repository_path


from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution('data-kale').version
except DistributionNotFound:
    pass
