
# To check outdated packages

`pip list --outdated`

# to updated outdated packages

## Winodws

`pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_}`

## Linux

`pip3 list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U `

or

`pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U `



