# 5.Merge the dictionaries `dict1` and `dict2` into a new dictionary named `merged_dict`.

dict1={
    "Boy":"Lips",
    "Girl":"Dogy",
}

dict2={
    "Women":"Horse",
    "Men":"Cat",
}

merged_dict={**dict1,**dict2}

me={
    "Me":"💦💦"
}
merged_dict.update(me)
print(merged_dict)