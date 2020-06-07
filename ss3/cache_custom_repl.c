#include "cache.h"
#include "cache_custom_repl.h"

/* use this to determine the way to evict */
unsigned int get_custom_repl_index(struct cache_t *cp,
                                   md_addr_t set) {

   // this is where to get replacement data if it is per set
   // that is, just use the first blocks data
   // cp->sets[set].blks->custom_repl_data;

   // for the worst possible MRU replacement policy, just return way_no of first block
   return cp->sets[set].blks->way_no;

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

   return NONE;
}

/* use this to update the cache block replacement data field during a hit
 * that is used to help determine the replacement index above
 * use return enum to tell cache.c to move replacement index to head or tail */
enum repl_action custom_repl_data_access(struct cache_t *cp,
                                         md_addr_t set,
			                 struct cache_blk_t *blk) {
   enum repl_action action;

   action = NONE;
   if (blk->way_prev) {
      /* move this block to head of the way (MRU) list */
      action = HEAD;
   }

   return action;
}

/* use this to initialize the cache block replacement data field */
void init_custom_repl_data(struct cache_blk_t *blk, int way_index) {

   // for MRU replacement policy just store way no, though it should already be in way_no field
   blk->custom_repl_data = way_index;

}
