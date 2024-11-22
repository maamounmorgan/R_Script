import arcpy

ws=arcpy.GetParameterAsText(0)
# تحديد مسار الشكل
fc = arcpy.GetParameterAsText(1)

# تحديد أنواع الحقول المراد حذفها
exclude_types =arcpy.GetParameterAsText(2)

# تحديد البادئة المراد استبعادها لأسماء الحقول
exclude_prefix = arcpy.GetParameterAsText(3)
def delete_fields(table, exclude_types=[], exclude_prefix=""):
    """
    حذف الحقول التي تفي بـكلا الشرطين:
    * نوع الحقل موجود في قائمة `exclude_types`
    * اسم الحقل يبدأ بالبادئة `exclude_prefix`
    """
    fields_to_delete = []
    fields = arcpy.ListFields(table)

    for field in fields:
        if (field.type in exclude_types) and (field.name.startswith(exclude_prefix)):
            fields_to_delete.append(field.name)

    arcpy.DeleteField_management(fc, fields_to_delete)
    return fields_to_delete
  
  
  # حذف الحقول
delete_fields(fc, exclude_types, exclude_prefix)



