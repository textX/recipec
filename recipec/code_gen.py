from functools import partial
from os.path import abspath, dirname, join

from textx import (gen_file, generator, get_children_of_type,
                   get_output_filename)


@generator('recipe-plan', 'md')
def plan_generator(metamodel, model, output_path, overwrite, debug,
                   **custom_args):
    output_file = get_output_filename(model._tx_filename, output_path, 'md')
    gen_file(model._tx_filename, output_file,
             partial(model_export, model, output_file),
             overwrite)


def model_export(model, output_file):
    import jinja2
    plan, = get_children_of_type("Plan", model)

    all_ingredients = {}  # ingredientType -> count
    for e in get_children_of_type("PlanEntry", plan):
        for i in get_children_of_type("Ingredient", e.get_recipe()):
            all_ingredients[i.get_type()] = \
                all_ingredients.get(i.get_type(), 0.0) \
                + i.get_count_in_default_units(float(e.person_count))

    config = get_all(model, "Config")
    config = config[0]

    this_folder = dirname(abspath(__file__))
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(join(this_folder, "template")),
        trim_blocks=True,
        lstrip_blocks=True)
    template = jinja_env.get_template('plan.template')
    with open(output_file, 'w') as f:
        f.write(template.render(plan=plan, config=config,
                                all_ingredients=all_ingredients))


def get_all(model, what):
    lst = []
    for m in model._tx_model_repository.all_models.filename_to_model.values():
        lst = lst + get_children_of_type(what, m)
    return lst
