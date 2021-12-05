from app.anagram.db import redis


async def get_number_of_anagrams_redis() -> int:
    result = await redis.get('anagram_counter')
    return 0 if result is None else int(result)


async def set_number_of_anagrams_redis(value: int):
    if value == 1:
        await redis.set('anagram_counter', 1)
    else:
        await redis.set('anagram_counter', value)


def anagram_check(string1: str, string2: str) -> bool:
    return sorted(string1.lower()) == sorted(string2.lower())
