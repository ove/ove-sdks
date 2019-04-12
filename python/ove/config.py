from .ove import Space

# Configuration for local testing
_local_size = {
    'width': 4320,
    'height': 2424,
    'screen_rows': 3,
    'screen_cols': 3
}

# Configuration for Data Observatory and DO-Dev
_dodev_size = {
    'height': 4320,
    'width': 15360,
    'screen_rows': 2,
    'screen_cols': 4
}

_do_size = {
    'height': 4320,
    'width': 30720,
    'screen_rows': 4,
    'screen_cols': 16
}

local_space = Space(ove_host="localhost", space_name="LocalNine", control_port=8080, geometry=_local_size)
dodev = Space(ove_host="gdo-appsdev.dsi.ic.ac.uk", space_name="DODev", control_port=9080, geometry=_dodev_size)
doprod = Space(ove_host="gdo-appsdev.dsi.ic.ac.uk", space_name="DOCluster", control_port=9080, geometry=_do_size)
