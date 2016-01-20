# This file is part {{ cookiecutter.module_name }} module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool

def register():
    Pool.register(
        module='{{ cookiecutter.module_name }}', type_='model')
    Pool.register(
        module='{{ cookiecutter.module_name }}', type_='wizard')
    Pool.register(
        module='{{ cookiecutter.module_name }}', type_='report')
