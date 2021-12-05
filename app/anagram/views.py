from fastapi import HTTPException, APIRouter

from app.anagram.services import get_number_of_anagrams_redis, set_number_of_anagrams_redis, anagram_check

router_anagram = APIRouter()


@router_anagram.get('/is_anagram')
async def check_two_string_are_anagrams(string1: str, string2: str):
    if not string1.isalpha() or not string2.isalpha():
        raise HTTPException(status_code=422, detail='strings should only contains letters')

    is_anagram = anagram_check(string1, string2)
    value = await get_number_of_anagrams_redis()
    if is_anagram:
        value += 1
        await set_number_of_anagrams_redis(value)

    return {'is_anagram': is_anagram, 'number_of_anagrams': value}
