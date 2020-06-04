import typing as t


class CADModelSyncService:

    def _update_fields(
            self,
            instances_by_des: t.Dict[str, t.Dict[str, str]],
            instance: t.Callable,
            model: t.Callable,
    ):
        i = instances_by_des[instance.des]
        should_save = False
        for field in model.REQUIRED_FIELDS:
            if getattr(instance, field) != i[field]:
                setattr(instance, field, i[field])
                should_save = True
        if should_save:
            instance.save()
            return 1

    def _update_instances(
            self,
            intersection: t.Iterable[str],
            instances_by_des: t.Dict,
            model: t.Callable
    ) -> int:
        print(f'{intersection=}')
        print(f'{instances_by_des=}')
        updated = 0
        instances_to_update = model.objects.with_designations(intersection)
        for instance in instances_to_update:
            updated += self._update_fields(
                instances_by_des,
                instance,
                model
            )
        return updated

    def sync_instances(
            self,
            instances: t.List[t.Dict[str, str]],
            model: t.Callable
    ) -> t.Tuple:
        # print(f'{instances=}')
        # print(f'{model=}')
        instances_by_des = {
            i['des']: {k: v for k, v in i.items() if k in model.REQUIRED_FIELDS}
            for i in instances
        }
        received = set(instances_by_des)
        existing = set(model.objects.values_list('des', flat=True))

        updated = self._update_instances(
            existing.intersection(received),
            instances_by_des,
            model
        )
        created = model.objects.bulk_create(
            model(**instances_by_des[name]) for name in received - existing
        )

        return len(created), updated

    def associate_fields(self, cad_data: t.Dict[str, t.List]):
        field_names = cad_data['fields']
        data = cad_data['data']
        instances = []
        for obj in data:
            instances.append(
                dict(zip(field_names, obj))
            )
        return instances
