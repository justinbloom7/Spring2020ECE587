#include <math.h>

#include "cache.h"
#include "cache_custom_repl.h"

/* use this to determine the way to evict */
unsigned int get_custom_repl_index(struct cache_t *cp,
                                   md_addr_t set) {

   // this is where to get replacement data if it is per set
   // that is, just use the first blocks data
   // cp->sets[set].blks->custom_repl_data;

   // for the worst possible MRU replacement policy, just return way_no of first block
   // however, this won't be a true MRU policy because the ss3 code is not looking for
   // unused ways. I am not sure why it doesn't do this.
   // TODO: make it so ss3 code will look for empty block before replacement
   //return cp->sets[set].blks->way_no;

   // PLRU IMPLEMENTATION
   // this is currently set up to work with associativity as a power of 2 (but not 1, or 2**0)
   int plruBits, index, levelCount, currentLevel, mask, levMask;

   levelCount = log2(cp->assoc) - 1; // make this 0 based (so 0 is actually 1 level)
   mask = (1 << (cp->assoc - 1)) - 1;
   // since only one set of PLRU bits per set, just use first block data 
   // since PLRU tree points to MRU, invert the bits to find pseudo LRU
   plruBits = cp->sets[set].blks->custom_repl_data ^ mask;
   levMask = 1;
   index = plruBits & levMask;
   for (currentLevel = 0; currentLevel < levelCount; ++currentLevel) {
      levMask = levMask << (1 << currentLevel); // points to start of level of tree
      mask = levMask << index;
      index = index << 1;
      if (plruBits & mask) {
         ++index;
      }
   }

   return index;
}

/* use this to update the cache block replacement data field during a miss
 * that is used to help determine the replacement index above
 * use return enum to tell cache.c to move replacement index to head or tail */
enum repl_action update_custom_repl_data(struct cache_t *cp,
                                         md_addr_t set) {

   // this code is for rotate replacement policy
   //if (cp->sets[set].blks->custom_repl_data < cp->assoc) {
      //++cp->sets[set].blks->custom_repl_data;
   //} else {
      //cp->sets[set].blks->custom_repl_data = 0;
   //}
 
   // do nothing for MRU replacement policy

   // do nothing for PLRU replacement policy

   return NONE;
}

/* use this to update the cache block replacement data field during a hit
 * that is used to help determine the replacement index above
 * use return enum to tell cache.c to move replacement index to head or tail */
enum repl_action custom_repl_data_access(struct cache_t *cp,
                                         md_addr_t set,
			                 struct cache_blk_t *blk) {
   enum repl_action action;

   // MRU replacement policy
   //action = NONE;
   //if (blk->way_prev) {
      /* move this block to head of the way (MRU) list */
      //action = HEAD;
   //}

   // PLRU replacement policy
   int plruBits, index, indexMask, levelCount, levMask, currentLevel;
   int andMask, orMask, treeIndexMask, treeIndex, maskBit;

   index = blk->way_no;
   levelCount = log2(cp->assoc) - 1; // make this 0 based (so 0 is actually 1 level)
   indexMask = 1 << levelCount; // i.e. 1 for levelCount = 0, 2 for levelCount = 1, etc.
   treeIndexMask = indexMask;
   levMask = 1;
   andMask = (1 << (cp->assoc - 1)) - 2; // subtract by 2 to always clear bit 0
   orMask = ((index & indexMask) == 1); // set low bit of orMask to high bit of index

   for (currentLevel = 0; currentLevel < levelCount; ++currentLevel) {
      levMask = levMask << (1 << currentLevel); // points to start of level of tree
      treeIndex = (index & treeIndexMask) >> (levelCount - currentLevel);
      maskBit = levMask << treeIndex;
      andMask ^= maskBit;  // always clear mask bit from andBit
      indexMask = indexMask >> 1;
      if (index & indexMask) {
         orMask |= maskBit; // set bit in orMask if it was set in index
      }
      treeIndexMask |= indexMask;
   }
   // since only one set of PLRU bits per set, just use first block data 
   plruBits = cp->sets[set].blks->custom_repl_data & andMask; // keep unaffected bits unchanged
   cp->sets[set].blks->custom_repl_data = plruBits | orMask;  // change affected bits
   action = NONE; // do not ever need to rearrange ways

   return action;
}

/* use this to initialize the cache block replacement data field */
void init_custom_repl_data(struct cache_blk_t *blk, int way_index) {

   // for MRU replacement policy just store way no, though it should already be in way_no field
   //blk->custom_repl_data = way_index;

   // for PLRU replacement policy, set data to 0 (all will be ignored except for first block in set)
   blk->custom_repl_data = 0;

}
