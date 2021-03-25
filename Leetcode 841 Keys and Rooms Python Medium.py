# Link to video: https://youtu.be/Ao4gpHs1WNw

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        room_seen = {key: False for key in range(n)}
        room_graph = {key: rooms[key] for key in range(n)}
        
        def rec(key):
            if room_seen[key]:
                return
            room_seen[key] = True
            for key2 in room_graph[key]:
                rec(key2)
        
        rec(0)
        if False in [room_seen[k] for k in room_seen]:
            return False
        return True