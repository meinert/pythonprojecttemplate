from dataclasses import dataclass, asdict, astuple, fields
import datetime


@dataclass
class DefaultProduct:
    ean: int = None
    brand: str = None
    price: float = None
    priceScore: float = None
    productUrl: str = None
    productName: str = None
    stock: str = None
    freight: float = -1
    productId: str = None
    updated: datetime = None
    store: str = None
    category: str = None
    deliveryTime: str = None
    imageUrl: str = None
    eanValid: bool = None
    totalScore: int = None
    status: str = None
    key: str = None
    productLink: str = None


@dataclass
class DimensionProduct:
    height: float = None
    length: float = None
    width: float = None
    weight: float = None
    heightScore: float = None
    lengthScore: float = None
    widthScore: float = None
    weightScore: float = None


@dataclass
class DimensionPackedProduct:
    packHeight: float = None
    packWidth: float = None
    packLength: float = None
    packShape: str = None
    packVolume: float = None
    packHeightScore: float = None
    packWidthScore: float = None
    packVolumeScore: float = None

    def __init__(self, pack_height=None, pack_width=None, pack_shape=None, pack_length=None):
        self.packHeight = pack_height
        self.packWidth = pack_width
        self.packLength = pack_length
        self.packShape = pack_shape
        self.packVolume = self.calculate_pack_vol()

    def calculate_pack_vol(self):
        if self.packShape == 'Cylinder':
            return pi * self.packWidth/2 * self.packWidth/2 * self.packHeight / 1000  # pi * radius^2 * height converted to Liter
        elif self.packShape == 'Box':
            return self.packLength * self.packWidth * self.packHeight / 1000


@dataclass
class Liggeunderlag(DefaultProduct, DimensionProduct, DimensionPackedProduct):
    rvalue: float = None
    rvalueScore: float = None
    type: str = None  # TODO: rename to subclass

    def __iter__(self):
        return iter(astuple(self))


def to_dict(data):
    return asdict(data)


def dict_to_dataclass(dict_to_cast, data_class):
    if data_class == 'liggeunderlag':
        try:
            return Liggeunderlag(**dict_to_cast[1])
        except Exception:
            return Liggeunderlag(**dict_to_cast)
    else:
        print('Product type: {} not supported yet'.format(data_class))
        return None
