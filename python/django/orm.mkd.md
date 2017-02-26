# ORM
## define a model
```python
from django.db import models
class ModelName(models.Model):
    field_one = models.IntegerField(primary_key = True, default = 0)
    field_two = models.CharField(max_length = 100)
    field_three = DateTimeField(auto_now_add=True)
    field_four = models.ForeignKey(AnotherModel, blank = True, null = True)
    ...
    
    class Meta:
        unique_together = ('field_one', 'field_two')
        index_together = [['field_one', 'field_two'], ]
```

* `auto_now_add`: init the value as the time when the object is saved.
* `auto_now`: update the value when the object is modified.

This model will create a table named as `app_modelname` when you run `python manage.py syncdb` under your root directory of your django project. 

## Query Set
### select
```python
query_set = Foo.objects.values()
```
### group by
```python
query_set = Foo.objects.values('userid'
        ).annotate(
        link_num = Count('userid')
        ).order_by('link_num')[0:20]
```

```sql
select count(*) as link_num
from app_foo
group by userid
order by link_num
offset 0 limit 20; 
```

