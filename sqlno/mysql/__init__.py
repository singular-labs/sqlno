from sqlno.common.aliases import (astrix, set_, gte, p, is_not, null, ne, or_, and_, is_)
from sqlno.common.functions import if_, values, coalesce, current_timestamp
from sqlno.common.statements import select
from sqlno.common.structures import Table
from sqlno.common.expressions import case, case_when
from sqlno.mysql.statements import insert_into

t = Table
