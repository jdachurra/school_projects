#ifndef DATASTRUCTURES_HH
#define DATASTRUCTURES_HH

#include "customtypes.hh"
#include <utility>
#include <vector>
#include <iterator>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>

template <typename Type>
Type random_in_range(Type start, Type end);


// This is the class you are supposed to implement
struct Place {
    PlaceID id;
    Coord coords;
    Name name;
    PlaceType type;
    double distance_euclidean;

    Place(PlaceID id, Coord coords, Name name, PlaceType type, double distance_euclidean)
        : id(id), coords(coords), name(name), type(type), distance_euclidean(distance_euclidean) {}
};

struct Area
{
    AreaID id;
    Name name;
    std::vector<Coord> coords;
    std::vector<AreaID> sub_areas;
};

struct Way
{
    WayID id;
    
    std::vector<Coord> coords;

    //Coord start_coord = coords.front();
    //Coord end_coord = coords.back();

    Way() = default;

        Way(WayID id, std::vector<Coord> coords)
        : id(id), coords(coords) {}

};

class Datastructures
{
public:
    Datastructures();
    ~Datastructures();

    // Estimate of performance: O(1)
    // Short rationale for estimate: Getting size of an unordered map is constant
    unsigned int get_place_count();

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    void clear_all();

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<PlaceID> all_places();

    // Estimate of performance: O(log(n))
    // Short rationale for estimate: 
    // The function inserts a new place into a map . 
    // Insertion into a balanced binary search tree is O(log(n)).
    bool add_place(PlaceID id, Name const& name, PlaceType type, Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    Name get_place_name(PlaceID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: retriving from a map is linear
    PlaceType get_place_type(PlaceID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: retriving from a map is linear
    Coord get_place_coord(PlaceID id);

    // We recommend you implement the operations below only after implementing the ones above

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<PlaceID> get_places_alphabetically();

    // Estimate of performance: O(n*log(n))
    // Short rationale for estimate: sorting is O(n*log(n))
    std::vector<PlaceID> get_places_distance_increasing();

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<PlaceID> find_places_with_coord(Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<PlaceID> find_places_with_name(Name const& name);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<PlaceID> find_places_with_type(PlaceType type);

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    bool change_place_name(PlaceID id, const Name& newname);

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    bool change_place_coord(PlaceID id, Coord newcoord);

    // We recommend you implement the operations below only after implementing the ones above

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    bool add_area(AreaID id, Name const& name, std::vector<Coord> coords);

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    std::vector<AreaID> all_areas();

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    Name get_area_name(AreaID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    std::vector<Coord> get_area_coords(AreaID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: function retrieves from a map
    bool add_subarea_to_area(AreaID id, AreaID parentid);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<AreaID> ancestor_areas_of_subarea(AreaID id);

    // Non-compulsory operations

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<AreaID> all_subareas_of_area(AreaID id);

    // Estimate of performance: O(n*log(n))
    // Short rationale for estimate: sorting is O(n*log(n))
    std::vector<PlaceID> get_places_closest_to(Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    bool remove_place(PlaceID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    AreaID get_closest_common_ancestor_of_areas(AreaID id1, AreaID id2);







    // prg2 functions

    // Estimate of performance: O(n)
    // Short rationale for estimate: Getting size of an unordered map is linear
    std::vector<WayID> all_ways();

    // Estimate of performance: O(1)
    // Short rationale for estimate: Getting size of an unordered map is constant
    bool add_way(WayID id, std::vector<Coord> coords);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<std::pair<WayID, Coord>> get_ways_from(Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    std::vector<Coord> get_way_coords(WayID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: iterating through unordered map is linear
    void clear_ways();

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: implement BFS potential
    std::vector<std::tuple<Coord, WayID, Distance>> route_any(Coord fromxy, Coord toxy);









    // prg2-opt functions

    // Estimate of performance:
    // Short rationale for estimate:
    std::vector<std::tuple<Coord, WayID, Distance>> route_shortest_distance(Coord fromxy, Coord toxy);

    // Estimate of performance:
    // Short rationale for estimate:
    std::vector<std::tuple<Coord, WayID, Distance>> route_least_crossroads(Coord fromxy, Coord toxy);

    // Estimate of performance:
    // Short rationale for estimate:
    std::vector<std::tuple<Coord, WayID>> route_with_cycle(Coord fromxy);

    // Estimate of performance:
    // Short rationale for estimate:
    Distance trim_ways();



private:
 
    std::unordered_map<PlaceID, Place> places_data;
    std::unordered_map<AreaID, Area> area_data;
    std::unordered_map<AreaID, AreaID> sub_to_parent;
    std::unordered_map<PlaceID, AreaID> place_to_area;
    std::unordered_map<Coord, PlaceID> coord_to_placeID;

    std::vector<PlaceID> place_ids;

    bool places_sorted_alphabetically_;
    bool places_sorted_by_distance_;

    double get_distance_euclidean(const Coord& xy) const;
    

    //PROJ2

    std::unordered_map<WayID, Way> ways_map;
    //std::vector<WayID> way_ids;
    //std::unordered_map<WayID, > connected_ways;
    

    std::unordered_map<Coord,  std::unordered_map<Coord, std::vector<std::tuple<Coord, WayID, Distance>>>> dijkstra_cache;

    //std::vector<std::tuple<Coord, WayID, Distance>> route_any_helper(Coord fromxy, Coord toxy, std::vector<WayID> way_ids);
    double get_distance_euclidean_complete(const Coord& xy1, const Coord& xy2) const;
    double get_way_distance(WayID id);


    std::vector<std::vector<WayID>> connected_ways_vector;

};

#endif // DATASTRUCTURES_HH
