"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args) -> list:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons) -> list:
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    a,b,c,*fixed_list_of_wagon = each_wagons_id
    return [c,*missing_wagons,*fixed_list_of_wagon,a,b]


def add_missing_stops(route, **kwargs) -> dict:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stops_list = []
    for key, value in kwargs.items():
        stops_list.append(value)
    stops_dict = {"stops":stops_list}
    final_dict = {**route,**stops_dict} 
    return final_dict


def extend_route_information(route, more_route_information) -> dict:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    updated_route = {**route, **more_route_information}
    return updated_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    # a,b,c, = zip(*wagons_rows)
    # return [list(a),list(b),list(c)]
    return [list(item) for item in zip(*wagons_rows)]
