#ifndef CUSTOM_CACHE_REPL_H
#define CUSTOM_CACHE_REPL_H

#include "cache.h"
#include "cache_custom_repl_data.h"

enum repl_action { NONE, HEAD, TAIL };

unsigned int get_custom_repl_index(struct cache_t *cp,
                                   md_addr_t set);
enum repl_action update_custom_repl_data(struct cache_t *cp,
                                         md_addr_t set);
enum repl_action custom_repl_data_access(struct cache_t *cp,
                                         md_addr_t set,
			                 struct cache_blk_t *blk);
void init_custom_repl_data(struct cache_blk_t *blk,
		           int way_index);

#endif
