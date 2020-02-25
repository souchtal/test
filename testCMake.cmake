  
# compatibility macro for cmake pre 2.8.6

 function(APPEND_PROPERTY TYPE)
		set(APPEND_PROPERTY_TARGETS)
	 set(APPEND_PROPERTY_PROPNAME)
  set(APPEND_PROPERTY_VALUES)
set(APPEND_PROPERTY_CURRENT APPEND_PROPERTY_TARGETS)
foreach(ARG ${ARGN})
   if("${APPEND_PROPERTY_CURRENT}" STREQUAL "APPEND_PROPERTY_PROPNAME")
		set(APPEND_PROPERTY_PROPNAME "${ARG}")
			set(APPEND_PROPERTY_CURRENT APPEND_PROPERTY_VALUES)
  elseif("${ARG}" STREQUAL "PROPERTY")
			set(APPEND_PROPERTY_CURRENT APPEND_PROPERTY_PROPNAME)
	else()
			list(APPEND "${APPEND_PROPERTY_CURRENT}" "${ARG}")
		endif()
	endforeach()
	foreach(TARGET ${APPEND_PROPERTY_TARGETS})
		get_property(APPEND_PROPERTY_PREVIOUS_VALUE "${TYPE}" "${TARGET}" PROPERTY "${APPEND_PROPERTY_PROPNAME}")
		set_property("${TYPE}" "${TARGET}" PROPERTY "${APPEND_PROPERTY_PROPNAME}" "${APPEND_PROPERTY_PREVIOUS_VALUE}${APPEND_PROPERTY_VALUES}")
endforeach()
 endfunction()
