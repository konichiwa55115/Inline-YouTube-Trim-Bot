#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
class Config:
    API_ID = int(os.environ.get("API_ID", '17983098'))
    API_HASH = os.environ.get("API_HASH", "ee28199396e0925f1f44d945ac174f64")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6089522865:AAG0vUsYSBg-BaSfiG1T5E1QTrorjoMDA4U")     
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", '-1001683878954'))
