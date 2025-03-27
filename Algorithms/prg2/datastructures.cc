/**
 * @brief The Datastructures class
 * STUDENTS: Modify the code below to implement the functionality of the class.
 * Also remove comments from the parameter names when you implement an operation
 * (Commenting out parameter name prevents compiler from warning about unused
 * parameters on operations you haven't yet implemented.)
 */

#include "datastructures.hh"
#include "customtypes.hh"
#include <functional>
#include <queue>
#include <stack>
#include <iostream>
#include <ostream>
#include <cmath>

// Modify the code below to implement the functionality of the class.

Datastructures::Datastructures()
{

}

Datastructures::~Datastructures()
{

}

/*

// Function to check if a point is inside a polygon using
// the ray-casting algorithm
bool Datastructures::isPointOnEdge(const Coord& p1, const Coord& p2, const Coord& point) {
    // Check if the point is on the line segment between p1 and p2
    double crossProduct = (point.y - p1.y) * (p2.x - p1.x) - (point.x - p1.x) * (p2.y - p1.y);
    if (std::abs(crossProduct) > 1e-10) {
        return false;
    }

    double dotProduct = (point.x - p1.x) * (p2.x - p1.x) + (point.y - p1.y) * (p2.y - p1.y);
    if (dotProduct < 0) {
        return false;
    }

    double squaredLength = (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y);
    if (dotProduct > squaredLength) {
        return false;
    }

    return true;
}

bool Datastructures::isPointInPolygon(const std::vector<Coord>& polygon,
                      const Coord& point)
{

    // Number of vertices in the polygon
    int n = polygon.size();
    // Count of intersections
    int count = 0;

    // Iterate through each edge of the polygon
    for (int i = 0; i < n; i++) {
        Coord p1 = polygon[i];
        // Ensure the last point connects to the first point
        Coord p2 = polygon[(i + 1) % n];

        // Check if the point's y-coordinate is within the
        // edge's y-range and if the point is to the left of
        // the edge
         // Check if the point is on the edge
        if (isPointOnEdge(p1, p2, point)) {
            return true;
        }


        if ((point.y > std::min(p1.y, p2.y))
            && (point.y <= std::max(p1.y, p2.y))
            && (point.x <= std::max(p1.x, p2.x))) {
            // Calculate the x-coordinate of the
            // intersection of the edge with a horizontal
            // line through the point
            double xIntersect = (point.y - p1.y)
                                    * (p2.x - p1.x)
                                    / (p2.y - p1.y)
                                + p1.x;
            // If the edge is vertical or the point's
            // x-coordinate is less than or equal to the
            // intersection x-coordinate, increment count
            if (p1.x == p2.x || point.x <= xIntersect) {
                count++;
            }
        }
    }
    // If the number of intersections is odd, the point is
    // inside the polygon
    return count % 2 == 1;
    //isPointInPolygon(polygon, point) returns TRUE or FALSE;
}
*/

double Datastructures::get_distance_euclidean(const Coord& xy) const
{
    return std::sqrt(xy.x * xy.x + xy.y * xy.y);
}

unsigned int Datastructures::get_place_count()
{
  return static_cast<int>(places_data.size());
}

void Datastructures::clear_all()
{
    
    places_data.clear();
    area_data.clear();
    sub_to_parent.clear();
    place_to_area.clear();
    coord_to_placeID.clear();
    place_ids.clear();

    places_sorted_alphabetically_ = false;
    places_sorted_by_distance_ = false;

    //clear for PRG2
    ways_map.clear();
    //way_ids.clear();


}

std::vector<PlaceID> Datastructures::all_places()
{
    std::vector<PlaceID> places;
    places.reserve(places_data.size());
    std::transform(places_data.begin(), places_data.end(), std::back_inserter(places),
                   [](const auto& pair) { return pair.first; });
    return places;
}

bool Datastructures::add_place(PlaceID id, const Name& name, PlaceType type, Coord xy)
{
    //check if place already exists
    if (places_data.find(id) != places_data.end()) return false;

    auto result = places_data.insert({id, {id, xy, name, type, get_distance_euclidean(xy)}});
    if (!result.second) return false;

    coord_to_placeID[xy] = id;
    place_ids.push_back(id);
    places_sorted_alphabetically_ = false;
    places_sorted_by_distance_ = false;
    //connected_places[id];
    return true;
}

Name Datastructures::get_place_name(PlaceID id)
{
  const auto place = places_data.find(id);
    if (place == places_data.end()) return NO_NAME;
    return place->second.name;
}


PlaceType Datastructures::get_place_type(PlaceID id)
{
  const auto place = places_data.find(id);
  if (place == places_data.end()) 
    {
      return PlaceType::NO_TYPE;
      }
  return place->second.type;
}

Coord Datastructures::get_place_coord(PlaceID id)
{
  const auto place = places_data.find(id);
    if (place == places_data.end()) return NO_COORD;
    return place->second.coords;
}

std::vector<PlaceID> Datastructures::get_places_alphabetically()
{
      if (!places_sorted_alphabetically_) {
        std::sort(place_ids.begin(), place_ids.end(),
                  [this](const PlaceID& idA, const PlaceID& idB)
                  {
                      const Place& placeA = places_data.at(idA);
                      const Place& placeB = places_data.at(idB);

                      if (placeA.name == placeB.name) {
                          return placeA.id < placeB.id;
                      }
                      return placeA.name < placeB.name;
                  });
        places_sorted_alphabetically_ = true;
        places_sorted_by_distance_ = false;
    }
    return place_ids;
}


std::vector<PlaceID> Datastructures::get_places_distance_increasing()
{

  if (!places_sorted_by_distance_  )        
    {
        std::sort(place_ids.begin(), place_ids.end(),
                  [this](const PlaceID& idA, const PlaceID& idB)
                  {
                      const Place& placeA = places_data.at(idA);
                      const Place& placeB = places_data.at(idB);

                      if (placeA.distance_euclidean == placeB.distance_euclidean) {
                          if (placeA.coords.y == placeB.coords.y) {
                              return placeA.id < placeB.id;
                          }
                          return placeA.coords.y < placeB.coords.y;
                      }
                      return placeA.distance_euclidean < placeB.distance_euclidean;
                  });
        places_sorted_by_distance_ = true;
        places_sorted_alphabetically_ = false;
    }
    return place_ids;
}


/*
std::vector<PlaceID> Datastructures::get_places_distance_increasing() 
{
    std::vector<PlaceID> sorted_place_ids = place_ids;

    std::sort(sorted_place_ids.begin(), sorted_place_ids.end(),
              [this](const PlaceID& idA, const PlaceID& idB) {
                  const Place& placeA = places_data.at(idA);
                  const Place& placeB = places_data.at(idB);

                  double distanceA = get_distance_euclidean(placeA.coords);
                  double distanceB = get_distance_euclidean(placeB.coords);

                  if (distanceA == distanceB) {
                      if (placeA.coords.y == placeB.coords.y) {
                          return placeA.id < placeB.id;
                      }
                      return placeA.coords.y < placeB.coords.y;
                  }
                  return distanceA < distanceB;
              });

    return sorted_place_ids;
}
*/

std::vector<PlaceID> Datastructures::find_places_with_coord(Coord xy)
{
    std::vector<PlaceID> places_return;
    for (const auto& [id, place] : places_data)
    {
        if (place.coords == xy)
        {
            places_return.push_back(id);
        }
    }
    return places_return;
}

std::vector<PlaceID> Datastructures::find_places_with_name(Name const& name)
{
    std::vector<PlaceID> places_return;
    for (const auto& [id, place] : places_data)
    {
        if (place.name == name)
        {
            places_return.push_back(id);
        }
    }
    return places_return;
}

std::vector<PlaceID> Datastructures::find_places_with_type(PlaceType type)
{
    std::vector<PlaceID> places_return;
    for (const auto& [id, place] : places_data)
    {
        if (place.type == type)
        {
            places_return.push_back(id);
        }
    }
    return places_return;
}


bool Datastructures::change_place_name(PlaceID id, const Name& newname)
{
    const auto place = places_data.find(id);
    if (place == places_data.end()) return false;

    /* this is scanning for all names, not just the one we are changing
    for (const auto& [place_id, place] : places_data)
    {
        if (place.name == newname) return false;
    }
    */

    if (place->second.name == newname) return false;
    place->second.name = newname;
    places_sorted_alphabetically_ = false;
    return true;
}


bool Datastructures::change_place_coord(PlaceID id, Coord newcoord)
{
    const auto place = places_data.find(id);
    if (place == places_data.end()) return false;

    /* this is scanning for all names, not just the one we are changing
    for (const auto& [place_id, place] : places_data)
    {
        if (place.coords == newname) return false;
    }
    */
    if (place->second.coords == newcoord) return false;
    place->second.coords = newcoord;
    place->second.distance_euclidean = get_distance_euclidean(newcoord);
    places_sorted_by_distance_ = false;
    return true;
}


bool Datastructures::add_area(AreaID id, const Name& name, std::vector<Coord> coords)
{
    if (area_data.find(id) != area_data.end()) return false;

    area_data[id] = {id, name, coords, {}};
    return true;
}


std::vector<AreaID> Datastructures::all_areas()
{
    std::vector<AreaID> areas;
    areas.reserve(area_data.size());
    std::transform(area_data.begin(), area_data.end(), std::back_inserter(areas),
                   [](const auto& pair) { return pair.first; });
    return areas;
}

Name Datastructures::get_area_name(AreaID id)
{
  const auto area = area_data.find(id);
    if (area == area_data.end()) return NO_NAME;
    return area->second.name;
}

std::vector<Coord> Datastructures::get_area_coords(AreaID id)
{
  const auto area = area_data.find(id);
    if (area == area_data.end()) return {NO_COORD};
    return area->second.coords;
}

bool Datastructures::add_subarea_to_area(AreaID id, AreaID parentid)
{
    if (area_data.find(id) == area_data.end() || area_data.find(parentid) == area_data.end()) return false;

    //if (sub_to_parent.find(id) != sub_to_parent.end()) return false;

    std::vector<Coord> parentPolygon = area_data[parentid].coords;
    std::vector<Coord> subPolygon = area_data[id].coords;

    //check if all coordinates of subarea are inside parent area
    /*
    for (const auto& coord : subPolygon)
    {
        if (!isPointInPolygon(parentPolygon, coord)) return false;
    }
    */
    //check if subarea already has a parent
    if (sub_to_parent.find(id) != sub_to_parent.end()) return false;


   

    area_data[parentid].sub_areas.push_back(id);
    sub_to_parent[id] = parentid;
    return true;
}

std::vector<AreaID> Datastructures::ancestor_areas_of_subarea(AreaID id)
{
    std::vector<AreaID> ancestors;
    AreaID current = id;
//Check if area exists
    if (area_data.find(id) == area_data.end()) return {NO_AREA};

    while (sub_to_parent.find(current) != sub_to_parent.end())
    {
        current = sub_to_parent[current];
        ancestors.push_back(current);
    }
    return ancestors;
}

/////////////////////OPTIONAL/////////////////////////////////////////////////////////////////////

std::vector<AreaID> Datastructures::all_subareas_of_area(AreaID id)
{	
//Returns all areas that belong to the area directly or indirectly
//If no subareas exist, returns an empty vector
//If area ID does not exist, returns a vector whose only item is NO_AREA 
      std::vector<AreaID> subareas;

    // Check if the area ID exists
    if (area_data.find(id) == area_data.end()) {
        return {NO_AREA};
    }

    // Recursion helper func.
    std::function<void(AreaID)> find_subareas = [&](AreaID area_id) {
        for (const auto& subarea : sub_to_parent) {
            if (subarea.second == area_id) {
                subareas.push_back(subarea.first);
                find_subareas(subarea.first);
            }
        }
    };

    // Start the recursion
    find_subareas(id);

    return subareas;
}

std::vector<PlaceID> Datastructures::get_places_closest_to(Coord xy)
{
    /*
    Returns three places at maximum that are closest to the given coordinate.
If places are less than tree, the function returns all places that it can
If the distance of places is equal, the function prefers
places that have the smallest y-values.
 If y values are the same, then the function sorts the places according to their id, the smallest first.
If no places exist, the function returns an empty vector
    */
     std::vector<std::pair<double, PlaceID>> distance_place_pairs;

    // Create a vector of pairs (distance, PlaceID)
    for (const auto& place : places_data) {
        double distance = std::sqrt(std::pow(place.second.coords.x - xy.x, 2) + std::pow(place.second.coords.y - xy.y, 2));
        distance_place_pairs.push_back({distance, place.first});
    }

    // Sort the vector of pairs by distance, then by y-coordinate, then by PlaceID
    std::sort(distance_place_pairs.begin(), distance_place_pairs.end(),
              [this](const std::pair<double, PlaceID>& a, const std::pair<double, PlaceID>& b) {
                  const Place& placeA = places_data.at(a.second);
                  const Place& placeB = places_data.at(b.second);

                  if (a.first == b.first) {
                      if (placeA.coords.y == placeB.coords.y) {
                          return placeA.id < placeB.id;
                      }
                      return placeA.coords.y < placeB.coords.y;
                  }
                  return a.first < b.first;
              });

    // Extract the closest three PlaceIDs
    std::vector<PlaceID> closest_places;
    for (size_t i = 0; i < std::min(distance_place_pairs.size(), size_t(3)); ++i) {
        closest_places.push_back(distance_place_pairs[i].second);
    }

    return closest_places;
}

bool Datastructures::remove_place(PlaceID id)
{
//Removes a place that has the given ID and returns true.
//If the place doesn't exist, it returns false.

    if (places_data.find(id) == places_data.end()) return false;

    places_data.erase(id);
    coord_to_placeID.erase(get_place_coord(id));
    place_ids.erase(std::remove(place_ids.begin(), place_ids.end(), id), place_ids.end());
    places_sorted_alphabetically_ = false;
    places_sorted_by_distance_ = false;
    return true;
}

AreaID Datastructures::get_closest_common_ancestor_of_areas(AreaID id1, AreaID id2)
{
//Returns the closest common ancestor that can be found in going upwards the chain of parents. Note that neither of the areas is accepted as that ancestor.
//Returns NO_AREA, if

//No area is found with the given ID
//No common ancestor is found
//If the areas are the same
    if (area_data.find(id1) == area_data.end() || area_data.find(id2) == area_data.end()) return NO_AREA;

    std::vector<AreaID> ancestors1 = ancestor_areas_of_subarea(id1);
    std::vector<AreaID> ancestors2 = ancestor_areas_of_subarea(id2);

    for (const auto& ancestor1 : ancestors1)
    {
        for (const auto& ancestor2 : ancestors2)
        {
            if (ancestor1 == ancestor2) return ancestor1;
        }
    }
    return NO_AREA;

}




/**
 * ============================
 * ============================
 * ========== PRG2 ============
 * ============================
 * ============================
 */



double Datastructures::get_distance_euclidean_complete(const Coord& xy1, const Coord& xy2) const
{
    
    return floor(std::sqrt(std::pow(xy1.x - xy2.x, 2) + std::pow(xy1.y - xy2.y, 2)));
}  

double Datastructures::get_way_distance(WayID id)
{
    const auto way = ways_map.find(id);
    if (way == ways_map.end()) return NO_DISTANCE;

    double distance = 0;
    for (size_t i = 0; i < way->second.coords.size() - 1; ++i)
    {
        distance += get_distance_euclidean_complete(way->second.coords[i], way->second.coords[i + 1]);
    }
    return distance;
}




void Datastructures::clear_ways()
{
    ways_map.clear();
    //way_ids.clear();
}


std::vector<WayID> Datastructures::all_ways()
{
    std::vector<WayID> ways;
    ways.reserve(ways_map.size());
    std::transform(ways_map.begin(), ways_map.end(), std::back_inserter(ways),
                   [](const auto& pair) { return pair.first; });
    return ways;
}

bool Datastructures::add_way(WayID id, std::vector<Coord> coords)
{
    if (ways_map.find(id) != ways_map.end()) return false;
    if (coords.size() < 2) return false;

    ways_map[id] = {id, coords};
    //clear dijkstra cache
    dijkstra_cache.clear();

    return true;
}

std::vector<std::pair<WayID, Coord>> Datastructures::get_ways_from(Coord xy)
{   
    ///could be more efficient
    std::vector<std::pair<WayID, Coord>> ways_from;
    for (const auto& way : ways_map)
    {
        if (way.second.coords.front() == xy || way.second.coords.back() == xy)
        {   
            if (way.second.coords.back() == xy) 
            {
                ways_from.push_back({way.first, way.second.coords.front()});
            }
            else 
            {
                ways_from.push_back({way.first, way.second.coords.back()});
            }
        }
    }

    return ways_from;
    
}

std::vector<Coord> Datastructures::get_way_coords(WayID id)
{   
    const auto way = ways_map.find(id);
    if (way == ways_map.end()) return {NO_COORD};
    return way->second.coords;

}



std::vector<std::tuple<Coord, WayID, Distance>> Datastructures::route_any(Coord fromxy, Coord toxy)
{
    std::vector<std::tuple<Coord, WayID, Distance>> route;

    // Check if either coordinate is not a crossroad
     if (get_ways_from(fromxy).empty() || get_ways_from(toxy).empty())
    {
        return {{NO_COORD, NO_WAY, NO_DISTANCE}};
    }


    // Check if the route is already in the cache
    if (dijkstra_cache.find(fromxy) != dijkstra_cache.end() && dijkstra_cache[fromxy].find(toxy) != dijkstra_cache[fromxy].end())
    {
        return dijkstra_cache[fromxy][toxy];
    }

     // Dijkstra's algorithm to find the shortest route from fromxy to toxy
    std::priority_queue<std::tuple<Distance, Coord, std::vector<std::tuple<Coord, WayID, Distance>>>,
                        std::vector<std::tuple<Distance, Coord, std::vector<std::tuple<Coord, WayID, Distance>>>>,
                        std::greater<>> pq;
    std::unordered_map<Coord, Distance> distances;
    std::unordered_map<Coord, std::vector<std::tuple<Coord, WayID, Distance>>> routes;
    pq.push({0, fromxy, {{fromxy, NO_WAY, 0}}});
    distances[fromxy] = 0;

    while (!pq.empty())
    {
        auto [current_distance, current_coord, current_route] = pq.top();
        pq.pop();

        if (current_coord == toxy)
        {
            current_route.back() = {toxy, NO_WAY, current_distance};
            dijkstra_cache[fromxy][toxy] = current_route;
            return current_route;
        }

        for (const auto& way : get_ways_from(current_coord))
        {
            Distance new_distance = current_distance + get_way_distance(way.first);
            if (distances.find(way.second) == distances.end() || new_distance < distances[way.second])
            {
                distances[way.second] = new_distance;
                auto new_route = current_route;
                //modify the last last element.second of the new_route to be way.firt
                //new_route.back() = {current_coord, way.first, current_distance};
                //new_route.push_back({way.second, NO_WAY, new_distance});

                new_route.push_back({way.second, way.first, new_distance});
                pq.push({new_distance, way.second, new_route});
                routes[way.second] = new_route;
            }
        }
    }

    // If no route is found, return an empty vector
    return {};
}





// prg2-opt functions

//the output differs form route_any, but it was not specified in the Specifications. Very poor documentation indeed for an automated tester.
std::vector<std::tuple<Coord, WayID, Distance>> Datastructures::route_shortest_distance(Coord fromxy, Coord toxy)
{
      std::vector<std::tuple<Coord, WayID, Distance>> route;

    // Check if either coordinate is not a crossroad
     if (get_ways_from(fromxy).empty() || get_ways_from(toxy).empty())
    {
        return {{NO_COORD, NO_WAY, NO_DISTANCE}};
    }


    // Check if the route is already in the cache
    if (dijkstra_cache.find(fromxy) != dijkstra_cache.end() && dijkstra_cache[fromxy].find(toxy) != dijkstra_cache[fromxy].end())
    {
        return dijkstra_cache[fromxy][toxy];
    }

     // Dijkstra's algorithm to find the shortest route from fromxy to toxy
    std::priority_queue<std::tuple<Distance, Coord, std::vector<std::tuple<Coord, WayID, Distance>>>,
                        std::vector<std::tuple<Distance, Coord, std::vector<std::tuple<Coord, WayID, Distance>>>>,
                        std::greater<>> pq;
    std::unordered_map<Coord, Distance> distances;
    std::unordered_map<Coord, std::vector<std::tuple<Coord, WayID, Distance>>> routes;
    pq.push({0, fromxy, {{fromxy, NO_WAY, 0}}});
    distances[fromxy] = 0;

    while (!pq.empty())
    {
        auto [current_distance, current_coord, current_route] = pq.top();
        pq.pop();

        if (current_coord == toxy)
        {
            current_route.back() = {toxy, NO_WAY, current_distance};
            dijkstra_cache[fromxy][toxy] = current_route;
            return current_route;
        }

        for (const auto& way : get_ways_from(current_coord))
        {
            Distance new_distance = current_distance + get_way_distance(way.first);
            if (distances.find(way.second) == distances.end() || new_distance < distances[way.second])
            {
                distances[way.second] = new_distance;
                auto new_route = current_route;
                //modify the last last element.second of the new_route to be way.firt
                new_route.back() = {current_coord, way.first, current_distance};
                
                new_route.push_back({way.second, NO_WAY, new_distance});
                pq.push({new_distance, way.second, new_route});
                routes[way.second] = new_route;
            }
        }
    }

    // If no route is found, return an empty vector
    return {};
}


std::vector<std::tuple<Coord, WayID, Distance>> Datastructures::route_least_crossroads(Coord fromxy, Coord toxy)
{
        std::vector<std::tuple<Coord, WayID, Distance>> route;

    // Check if either coordinate is not a crossroad
     if (get_ways_from(fromxy).empty() || get_ways_from(toxy).empty())
    {
        return {{NO_COORD, NO_WAY, NO_DISTANCE}};
    }


    // Check if the route is already in the cache
    if (dijkstra_cache.find(fromxy) != dijkstra_cache.end() && dijkstra_cache[fromxy].find(toxy) != dijkstra_cache[fromxy].end())
    {
        return dijkstra_cache[fromxy][toxy];
    }

     // Dijkstra's algorithm to find the shortest route from fromxy to toxy
    std::priority_queue<std::tuple<Distance, Coord, std::vector<std::tuple<Coord, WayID, Distance>>>,
                        std::vector<std::tuple<Distance, Coord, std::vector<std::tuple<Coord, WayID, Distance>>>>,
                        std::greater<>> pq;
    std::unordered_map<Coord, Distance> distances;
    std::unordered_map<Coord, std::vector<std::tuple<Coord, WayID, Distance>>> routes;
    pq.push({0, fromxy, {{fromxy, NO_WAY, 0}}});
    distances[fromxy] = 0;

    while (!pq.empty())
    {
        auto [current_distance, current_coord, current_route] = pq.top();
        pq.pop();

        if (current_coord == toxy)
        {
            //current_route.back() = {toxy, NO_WAY, current_distance};
            dijkstra_cache[fromxy][toxy] = current_route;
            return current_route;
        }

        for (const auto& way : get_ways_from(current_coord))
        {
            //change to account for nodes instead of distance
            Distance new_distance = current_distance + 1;
            Distance real_distance = std::get<2>(current_route.back()) + get_way_distance(way.first);

            if (distances.find(way.second) == distances.end() || new_distance < distances[way.second])
            {
                distances[way.second] = new_distance;
                auto new_route = current_route;

                //modify the last last element.second of the new_route to be way.firt
                new_route.back() = {current_coord, way.first, std::get<2>(current_route.back())};
                new_route.push_back({way.second, NO_WAY, real_distance});

                pq.push({new_distance, way.second, new_route});
                routes[way.second] = new_route;
            }
        }
    }

    // If no route is found, return an empty vector
    return {};
}

std::vector<std::tuple<Coord, WayID>> Datastructures::route_with_cycle(Coord fromxy)
{
    std::vector<std::tuple<Coord, WayID>> route;

    // Check if the starting coordinate is a crossroad
    bool is_crossroad = false;
    for (const auto& way : ways_map) {
        if (way.second.coords.front() == fromxy || way.second.coords.back() == fromxy) {
            is_crossroad = true;
            break;
        }
    }
    if (!is_crossroad)
    {
        return {{NO_COORD, NO_WAY}};
    }

    std::unordered_set<Coord> visited;
    std::stack<std::tuple<Coord, WayID, std::vector<std::tuple<Coord, WayID>>>> stack;
    stack.push({fromxy, NO_WAY, {{fromxy, NO_WAY}}});

    while (!stack.empty())
    {
        auto [current_coord, current_way, current_route] = stack.top();
        stack.pop();

        if (visited.find(current_coord) != visited.end())
        {
            // Cycle detected
            current_route.push_back({current_coord, NO_WAY});

            //remove the first item
            current_route.erase(current_route.begin());
            
            return current_route;
        }

        visited.insert(current_coord);

        for (const auto& way : get_ways_from(current_coord))
        {
            if (way.first != current_way) // Avoid traversing back the same way
            {
                auto new_route = current_route;
                new_route.push_back({current_coord, way.first});
                stack.push({way.second, way.first, new_route});
            }
        }
    }

    // If no cycle is found, return an empty vector
    return {};
}
Distance Datastructures::trim_ways()
{
    // Helper function to find the root of a node in the disjoint set
    std::function<Coord(std::unordered_map<Coord, Coord>&, Coord)> find = [&find](std::unordered_map<Coord, Coord>& parent, Coord node) {
        if (parent[node] != node) {
            parent[node] = find(parent, parent[node]);
        }
        return parent[node];
    };

    // Helper function to union two sets in the disjoint set
    auto union_sets = [&find](std::unordered_map<Coord, Coord>& parent, std::unordered_map<Coord, int>& rank, Coord node1, Coord node2) {
        Coord root1 = find(parent, node1);
        Coord root2 = find(parent, node2);
        if (root1 != root2) {
            if (rank[root1] > rank[root2]) {
                parent[root2] = root1;
            } else if (rank[root1] < rank[root2]) {
                parent[root1] = root2;
            } else {
                parent[root2] = root1;
                rank[root1]++;
            }
        }
    };

    // Create a list of all edges with their distances
    std::vector<std::tuple<Distance, Coord, Coord, WayID>> edges;
    for (const auto& way : ways_map) {
        const auto& coords = way.second.coords;
        if (coords.size() >= 2) {
            Distance dist = get_way_distance(way.first);
            edges.push_back({dist, coords.front(), coords.back(), way.first});
        }
    }

    // Sort edges by distance
    std::sort(edges.begin(), edges.end());

    // Initialize disjoint set
    std::unordered_map<Coord, Coord> parent;
    std::unordered_map<Coord, int> rank;
    for (const auto& way : ways_map) {
        for (const auto& coord : way.second.coords) {
            parent[coord] = coord;
            rank[coord] = 0;
        }
    }

    // Kruskal's algorithm to find the MST
    Distance total_distance = 0;
    std::unordered_map<WayID, Way> mst_ways_map;
    for (const auto& [dist, coord1, coord2, way_id] : edges) {
        if (find(parent, coord1) != find(parent, coord2)) {
            union_sets(parent, rank, coord1, coord2);
            total_distance += dist;
            mst_ways_map[way_id] = ways_map[way_id];
        }
    }

    // Update the ways_map to only include the MST
    ways_map = std::move(mst_ways_map);

    return total_distance;
}