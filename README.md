# sqlno

Just the closest to sql generating code, no tricks, no smart things. WYSIWYG!

## Examples:

you see:
```python
from sqlno.mysql import * 

select('*').from_('t_0 as t_a_0').where(c('t_a_0.c_0') > 2).semicolon(),
```
you get:
```
SELECT * FROM t_0 as t_a_0 WHERE t_a_0.c_0 > 2;
```
you can also see:
```python
from sqlno.mysql import * 

a_t_0 = t('t_0').as_('t_a_0')
c_0 = a_t_0.c_0

select('*').from_(a_t_0).where(c_0 > 2).semicolon(),
```
and get:
```
SELECT * FROM t_0 as t_a_0 WHERE t_a_0.c_0 > 2;
```

you see:
```python
from sqlno.mysql import * 

t_0 = t('t_0')
c_0 = c('c_0')
c_1 = c('c_1')

insert_into(
        t_0, c_0
    ).values([1]).on_duplicate_key_update(
        set_(c_1, if_(gte(values(c_0), coalesce(c_0, -1)), values(c_0), c_0))
    ).semicolon()
```
you get:
```
INSERT INTO t_0 (c_0) VALUES (1) ON DUPLICATE KEY UPDATE c_1 = if(values(c_0) >= coalesce(c_0, -1), values(c_0), c_0);
```
