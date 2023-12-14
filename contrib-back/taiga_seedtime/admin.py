# -*- coding: utf-8 -*-
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2021-present Kaleidos Ventures SL

from django.contrib import admin
from . import models


class GameAdmin(admin.ModelAdmin):
    list_display = ["project", "name", "uuid"]
    list_display_links = ["name"]
    raw_id_fields = ["project"]


admin.site.register(models.Game, GameAdmin)