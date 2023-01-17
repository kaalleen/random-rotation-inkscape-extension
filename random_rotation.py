#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2022 Kaalleen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from inkex import (EffectExtension, errormsg)
from random import choice, sample


class RandomRotation(EffectExtension):
    """
    This extension rotates random objects from a selection by user defined values.
    """
    def add_arguments(self, pars):
        pars.add_argument("--angle", type=str, default="60", help="Enter space separated list of angles", dest="angle")
        pars.add_argument("--num_elements", type=int, default=5, help="Rotate this amount of elements", dest="num_elements")

    def effect(self):
        selected = list(self.svg.selection)

        if not selected:
            errormsg("Please select at least one element.")
            return

        angles = self.options.angle.split(" ")
        angles = [float(num) for num in angles if self._is_float(num)]

        if self.options.num_elements > 0:
            n = min(len(selected), self.options.num_elements)
        else:
            n = choice(list(range(0, len(selected) + 1)))
        selected = sample(selected, n)

        for element in selected:
            angle = choice(angles)
            center = element.bounding_box(-element.transform).center
            element.transform.add_rotate(angle, center)

    def _is_float(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    RandomRotation().run()
