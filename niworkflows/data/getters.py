#!/usr/bin/env python
# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Data grabbers
"""
from __future__ import print_function, division, absolute_import, unicode_literals

from pathlib import Path
from ..data.utils import _get_dataset_dir, _fetch_file


OSF_PROJECT_URL = ('https://files.osf.io/v1/resources/fvuh8/providers/osfstorage/')
OSF_RESOURCES = {
    'MNI152NLin2009cAsym': ('5b0dbce20f461a000db8fa3d', '5d386d7db9c1dec30230623db25e05e1'),
    'OASIS30ANTs': ('5b0dbce34c28ef0012c7f788', 'f625a0390eb32a7852c7b0d71ac428cd'),
    'brainweb': ('57f32b96b83f6901f194c3ca', '384263fbeadc8e2cca92ced98f224c4b'),
    'ds003_downsampled': ('57f328f6b83f6901ef94cf70', '5a558961c1eb5e5f162696d8afa956e8'),
    'mni_template': ('57f32ab29ad5a101fb77fd89', 'debfa882b8c301cd6d75dd769e73f727'),
    'mni_template_RAS': ('57f32a799ad5a101f977eb77', 'a4669f0e7acceae148bb39450b2b21b4'),
    'ants_oasis_template': ('57f32ae89ad5a101f977eb79', '34d39070b541c416333cc8b6c2fe993c'),
    'ants_oasis_template_ras': ('584123a29ad5a1020913609d', 'afa21f99c66ae1672320d8aa0408229a'),
    'ants_nki_template_ras': ('59cd90f46c613b02b3d79782', 'e5debaee65b8f2c8971577db1327e314'),
    'mni_epi': ('57fa09cdb83f6901d93623a0', '9df727e1f742ec55213480434b4c4811'),
    'mni152_nlin_sym_las': ('57fa7fc89ad5a101e635eeef', '9c4c0cad2a2e99d6799f01abf4107f5a'),
    'mni152_nlin_sym_ras': ('57fa7fd09ad5a101df35eed0', '65d64ad5a980da86e7d07d95b3ed2ccb'),
    'mni_icbm152_linear': ('580705eb594d9001ed622649', '72be639e92532def7caad75cb4058e83'),
    'mni_icbm152_nlin_asym_09c': ('580705089ad5a101f17944a9', '002f9bf24dc5c32de50c03f01fa539ec'),
    'tpl-OASISTRT20': ('5b16f17aeca4a80012bd7542', '1b5389bc3a895b2bd5c0d47401107176'),
    'tpl-hcpLR32k': ('5b198ec6b796ba000f3e4858', '0ba9adcaa42fa88616a4cea5a1ce0c5a'),
    'tpl-conte69': ('5b198ec5ec24e20011b48548', 'bd944e3f9f343e0e51e562b440960529'),
}

BIDS_EXAMPLES = {
    'BIDS-examples-1-1.0.0-rc3u5': (
        'https://github.com/chrisfilo/BIDS-examples-1/archive/1.0.0-rc3u5.tar.gz',
        '035fe54445c56eff5bd845ef3795fd56'),
    'BIDS-examples-1-enh-ds054': (
        'http://github.com/chrisfilo/BIDS-examples-1/archive/enh/ds054.zip',
        '56cee272860624924bc23efbe868acb7'),
}

# Map names of templates to OSF_RESOURCES keys
TEMPLATE_MAP = {
    'MNI152NLin2009cAsym': 'MNI152NLin2009cAsym',
    'OASIS': 'OASIS30ANTs',
    'NKI': 'ants_nki_template_ras',
}


def get_dataset(dataset_name, data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the BIDS-fied brainweb 1mm normal


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    data_dir = _get_dataset_dir(dataset_name, data_dir=data_dir, verbose=verbose)

    if dataset_name in TEMPLATE_MAP:
        dataset_name = TEMPLATE_MAP.get(dataset_name, dataset_name)
        data_dir = str(Path(data_dir).parent / (
            'tpl-%s' % dataset_name))

    file_id, md5 = OSF_RESOURCES[dataset_name]
    if url is None:
        url = '{}/{}'.format(OSF_PROJECT_URL, file_id)

    if _fetch_file(url, data_dir, filetype='tar', resume=resume, verbose=verbose,
                   md5sum=md5):
        return data_dir
    else:
        return None


def get_brainweb_1mm_normal(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the BIDS-fied brainweb 1mm normal


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    return get_dataset('brainweb', data_dir, url, resume, verbose)


def get_ds003_downsampled(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the BIDS-fied ds003_downsampled


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    return get_dataset('ds003_downsampled', data_dir, url, resume, verbose)


def get_mni_template(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template


    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.

    """
    return get_dataset('mni_template', data_dir, url, resume, verbose)


def get_mni_template_ras(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni_template_RAS', data_dir, url, resume, verbose)


def get_mni_epi(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni_epi', data_dir, url, resume, verbose)


def get_ants_oasis_template(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the ANTs template of the OASIS dataset.
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('ants_oasis_template', data_dir, url, resume, verbose)


def get_ants_oasis_template_ras(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the ANTs template of the OASIS dataset.
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('ants_oasis_template_ras', data_dir, url, resume, verbose)


def get_ants_nki_template_ras(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the ANTs template of the NKI dataset.
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('ants_nki_template_ras', data_dir, url, resume, verbose)


def get_mni152_nlin_sym_las(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni152_nlin_sym_las', data_dir, url, resume, verbose)


def get_mni152_nlin_sym_ras(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni152_nlin_sym_ras', data_dir, url, resume, verbose)


def get_mni_icbm152_nlin_asym_09c(data_dir=None, url=None, resume=True, verbose=1):
    return get_dataset('mni_icbm152_nlin_asym_09c', data_dir, url, resume, verbose)


def get_mni_icbm152_linear(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the mni template
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('mni_icbm152_linear', data_dir, url, resume, verbose)


def get_bids_examples(data_dir=None, url=None, resume=True, verbose=1, variant=None):
    """
    Download BIDS-examples-1
    """

    if variant is None or variant not in BIDS_EXAMPLES:
        variant = 'BIDS-examples-1-1.0.0-rc3u5'

    if url is None:
        url = BIDS_EXAMPLES[variant][0]
    md5 = BIDS_EXAMPLES[variant][1]
    data_dir = _get_dataset_dir(variant, data_dir=data_dir, verbose=verbose)

    if _fetch_file(url, data_dir, filetype=None, resume=resume, verbose=verbose,
                   md5sum=md5):
        return data_dir
    else:
        return None


def get_oasis_dkt31_mni152(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files from the Mindboggle DKT31 label
    atlas in MNI152NLin2009cAsym space
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('tpl-OASISTRT20', data_dir, url, resume, verbose)


def get_hcp32k_files(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load the necessary files for conversion between fsaverage5/6
    and fs_LR(32k)
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('tpl-hcpLR32k', data_dir, url, resume, verbose)


def get_conte69_mesh(data_dir=None, url=None, resume=True, verbose=1):
    """Download and load Conte69-atlas meshes in 32k resolution
    :param str data_dir: path of the data directory. Used to force data storage
        in a non-standard location.
    :param str url: download URL of the dataset. Overwrite the default URL.
    """
    return get_dataset('tpl-conte69', data_dir, url, resume, verbose)
