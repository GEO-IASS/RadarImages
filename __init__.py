# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RadarImages
                                 A QGIS plugin
 Load and visualize radar images
                             -------------------
        begin                : 2015-09-17
        copyright            : (C) 2015 by Zia Mohammed
        email                : mohammed.zia33@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RadarImages class from file RadarImages.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .radar_images import RadarImages
    return RadarImages(iface)
