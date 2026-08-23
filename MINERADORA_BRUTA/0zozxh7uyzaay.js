;!function(){try { var e="undefined"!=typeof globalThis?globalThis:"undefined"!=typeof global?global:"undefined"!=typeof window?window:"undefined"!=typeof self?self:{},n=(new e.Error).stack;n&&((e._debugIds|| (e._debugIds={}))[n]="3cfc77e5-ca70-08c1-17b4-3ac26a1d222d")}catch(e){}}();
(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,822262,e=>{e.v({providerTable:"AiIntegrationsSection-module__Ok0YOW__providerTable",providerTableDisabled:"AiIntegrationsSection-module__Ok0YOW__providerTableDisabled",settingRowContent:"AiIntegrationsSection-module__Ok0YOW__settingRowContent"})},299560,e=>{e.v({description:"HasCredentialsSwitch-module__5n9FFa__description",optionCard:"HasCredentialsSwitch-module__5n9FFa__optionCard",optionCardContent:"HasCredentialsSwitch-module__5n9FFa__optionCardContent",optionsContainer:"HasCredentialsSwitch-module__5n9FFa__optionsContainer",radioButton:"HasCredentialsSwitch-module__5n9FFa__radioButton",selected:"HasCredentialsSwitch-module__5n9FFa__selected",title:"HasCredentialsSwitch-module__5n9FFa__title"})},194751,e=>{e.v({groupBadge:"ConnectorsOrgGroupSelect-module__YlgsWq__groupBadge",groupIcon:"ConnectorsOrgGroupSelect-module__YlgsWq__groupIcon"})},610446,e=>{e.v({form:"OrgConnectorUpdateForm-module__ZqHDNa__form"})},242001,e=>{e.v({deleteCard:"OrgManageConnectorModal-module__0SAr7G__deleteCard",divider:"OrgManageConnectorModal-module__0SAr7G__divider",header:"OrgManageConnectorModal-module__0SAr7G__header",imageContainer:"OrgManageConnectorModal-module__0SAr7G__imageContainer",modal:"OrgManageConnectorModal-module__0SAr7G__modal",replSection:"OrgManageConnectorModal-module__0SAr7G__replSection",tabsContainer:"OrgManageConnectorModal-module__0SAr7G__tabsContainer"})},68177,e=>{e.v({connectorIcon:"ConfiguredConnectors-module__zOUr5a__connectorIcon",headerContainer:"ConfiguredConnectors-module__zOUr5a__headerContainer",searchBar:"ConfiguredConnectors-module__zOUr5a__searchBar",searchBarFull:"ConfiguredConnectors-module__zOUr5a__searchBarFull"})},534033,e=>{e.v({form:"OrgConnectorSetupForm-module__8B8tSW__form",logoContainer:"OrgConnectorSetupForm-module__8B8tSW__logoContainer"})},553780,e=>{e.v({cardContainer:"ConnectorSetup-module__v7WxDW__cardContainer",connectorGrid:"ConnectorSetup-module__v7WxDW__connectorGrid",connectorSetup:"ConnectorSetup-module__v7WxDW__connectorSetup",emptyState:"ConnectorSetup-module__v7WxDW__emptyState",headerContainer:"ConnectorSetup-module__v7WxDW__headerContainer","loading-pulse":"ConnectorSetup-module__v7WxDW__loading-pulse",loadingSkeleton:"ConnectorSetup-module__v7WxDW__loadingSkeleton",loadingText:"ConnectorSetup-module__v7WxDW__loadingText",modal:"ConnectorSetup-module__v7WxDW__modal",searchBar:"ConnectorSetup-module__v7WxDW__searchBar",searchBarFull:"ConnectorSetup-module__v7WxDW__searchBarFull"})},953956,e=>{e.v({headerContainer:"Connectors-module__qFGIdW__headerContainer",searchControls:"Connectors-module__qFGIdW__searchControls",searchControlsFull:"Connectors-module__qFGIdW__searchControlsFull"})},28733,e=>{"use strict";var n=e.i(276385),t=e.i(389959),o=e.i(908796),r=e.i(29822),a=e.i(40916),i=e.i(255701),s=e.i(973245),l=e.i(304277);e.i(566901);var c=e.i(951262);let d={},u=s.gql`
    fragment CustomerAiIntegrationsSectionSettings on CustomerSettings {
  higherPowerModelDisabled
  modelfarmDisabled
  openrouterDisabled
  openaiDisabled
  anthropicDisabled
  geminiDisabled
}
    `,g=s.gql`
    query AiIntegrationsSection($orgId: String!) {
  currentUser {
    ... on CurrentUser {
      id
      org(orgId: $orgId) {
        ... on Org {
          id
          dealContext {
            dealType
          }
          authorizations {
            editSettings {
              isAuthorized
              message
            }
          }
          customer {
            ... on Customer {
              id
              authorizations {
                editSettings {
                  isAuthorized
                  message
                }
              }
              settings {
                ...CustomerAiIntegrationsSectionSettings
              }
            }
          }
        }
      }
    }
  }
}
    ${u}`,p=s.gql`
    mutation CustomerAiIntegrationsSectionUpdate($input: UpdateCustomerSettingsInput!) {
  updateCustomerSettings(input: $input) {
    __typename
    ... on Customer {
      id
      settings {
        ...CustomerAiIntegrationsSectionSettings
      }
    }
    ... on UnauthorizedError {
      message
    }
    ... on NotFoundError {
      message
    }
    ... on UserError {
      message
    }
  }
}
    ${u}`;var m=e.i(752007),h=e.i(827529),C=e.i(870496),x=e.i(951884),f=e.i(735362),_=e.i(609912),y=e.i(108431),S=e.i(327391),j=e.i(984119),v=e.i(508454),w=e.i(8047),b=e.i(244945),O=e.i(61732),T=e.i(822262);let N={highPowerModel:"higherPowerModelDisabled",modelfarm:"modelfarmDisabled",openrouter:"openrouterDisabled",openai:"openaiDisabled",anthropic:"anthropicDisabled",gemini:"geminiDisabled"},U={highPowerModel:null,modelfarm:null,openrouter:null,openai:null,anthropic:null,gemini:null},I=(e,n)=>{switch(n.type){case"TOGGLE_SETTING":return{...e,[n.key]:n.value};case"RESET_ALL":return U;default:return e}};function D({description:e}){return(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsxs)(O.View,{row:!0,gap:8,align:"center",children:[(0,n.jsx)(f.default,{size:24}),(0,n.jsx)(w.Header,{level:2,variant:"subheadBig",children:"Replit-managed AI Integrations"})]}),e?(0,n.jsx)(w.Text,{color:"dimmer",children:e}):null]})}let E=[{key:"name",label:"Provider",allowSorting:!1,isRowHeader:!0,width:200},{key:"enabled",label:"Enabled",allowSorting:!1,maxWidth:80}],A=({orgId:e})=>{var o;let r,a,{data:i,loading:s,error:u}=(o={variables:{orgId:e},ssr:!1},r={...d,...o},l.useQuery(g,r)),[f,{loading:A}]=(a={...d,...void 0},c.useMutation(p,a)),[V,k]=(0,t.useState)(null);(0,t.useEffect)(()=>{if(!V)return;let e=setTimeout(()=>k(null),5e3);return()=>clearTimeout(e)},[V]);let[F,M]=(0,t.useReducer)(I,U),R=i?.currentUser?.__typename==="CurrentUser"&&"Org"===i.currentUser.org.__typename?i.currentUser.org:null,B=R?.customer?.__typename==="Customer"?R.customer:null,q=B?.id??null,G=B?.authorizations.editSettings,$=G?.isAuthorized??!1,z=G?.message??"",P=R?.dealContext.dealType==="enterprise"||R?.dealContext.dealType==="enterprise_trial",W=B?.settings,L=W?.modelfarmDisabled??P,H=W?.openrouterDisabled??!1,Q=W?.openaiDisabled??!1,K=W?.anthropicDisabled??!1,Y=W?.geminiDisabled??!1,J=(e,n)=>{let t=F[e];return null!==t?t:!n},Z=J("modelfarm",L),X=J("openrouter",H),ee=J("openai",Q),en=J("anthropic",K),et=J("gemini",Y),eo=n=>t=>{k(null),M({type:"TOGGLE_SETTING",key:n,value:t}),null==q||f({variables:{input:{customerId:q,[N[n]]:!t}},refetchQueries:[{query:g,variables:{orgId:e}}],awaitRefetchQueries:!0,onCompleted:e=>{M({type:"RESET_ALL"}),"Customer"!==e.updateCustomerSettings.__typename&&k(e.updateCustomerSettings.message)},onError:()=>{M({type:"RESET_ALL"}),k("Failed to update AI settings")}})},er=eo("modelfarm"),ea=eo("openrouter"),ei=eo("openai"),es=eo("anthropic"),el=eo("gemini"),ec=[{name:"OpenRouter",icon:(0,n.jsx)(x.default,{}),isChecked:X,onChange:ea},{name:"OpenAI",icon:(0,n.jsx)(C.default,{}),isChecked:ee,onChange:ei},{name:"Anthropic",icon:(0,n.jsx)(m.default,{}),isChecked:en,onChange:es},{name:"Gemini",icon:(0,n.jsx)(h.default,{}),isChecked:et,onChange:el}];return s?null:u||!R?(0,n.jsxs)(O.View,{gap:8,children:[(0,n.jsx)(D,{}),(0,n.jsx)(y.StatusBanner,{text:"Failed to load AI integration settings. Please try again later.",colorway:"negative"})]}):(0,n.jsxs)(O.View,{gap:8,children:[(0,n.jsx)(D,{description:"Control which Replit-managed LLM providers are available to users in your workspace."}),(0,n.jsxs)(O.View,{gap:16,pt:8,children:[$?null:(0,n.jsx)(y.StatusBanner,{text:z,colorway:"warning"}),(0,n.jsx)(b.Tooltip,{tooltip:$?void 0:z,isDisabled:$,children:(0,n.jsxs)(O.View,{gap:16,children:[(0,n.jsxs)(O.View,{row:!0,gap:16,justify:"space-between",children:[(0,n.jsx)(O.View,{gap:4,clsx:T.default.settingRowContent,children:(0,n.jsx)(w.Text,{variant:"subheadDefault",children:"Allow users in the workspace to access Replit-managed LLM providers"})}),(0,n.jsx)(S.Switch,{isReadOnly:!$||A,"aria-label":"Replit-managed AI Integrations",isSelected:Z,onChange:er})]}),(0,n.jsx)(O.View,{gap:12,clsx:[T.default.providerTable,{[T.default.providerTableDisabled]:!Z}],children:(0,n.jsx)(_.IndexTable,{title:"",autoLayout:!1,columns:E,items:ec,children:e=>(0,n.jsxs)(v.TableRow,{id:e.name,children:[(0,n.jsx)(j.TableCell,{children:(0,n.jsxs)(O.View,{row:!0,gap:8,align:"center",children:[e.icon,(0,n.jsx)(w.Text,{translate:"no",children:e.name})]})},"name"),(0,n.jsx)(j.TableCell,{children:(0,n.jsx)(S.Switch,{isReadOnly:!$||A||!Z,"aria-label":`Toggle ${e.name}`,isSelected:e.isChecked,onChange:e.onChange})},"enabled")]},e.name)})})]})}),V?(0,n.jsx)(y.StatusBanner,{text:V,colorway:"negative"}):null]})]})};var V=e.i(70734),k=e.i(940306),F=e.i(723636),M=e.i(891093),R=e.i(151027),B=e.i(415541),q=e.i(709485),G=e.i(457145),$=e.i(415756),z=e.i(130902);let P={},W=s.gql`
    fragment OrgConnectorItem on OrgConnector {
  type
  name
  displayName
  logoUrl
  authType
  stage
  platforms
  credentials
  requiredScopes
  defaultScopes
  allowedScopes
  scopes {
    scope
    displayName
    description
  }
  schemas {
    connectorConfig
    connectionSettings
  }
}
    `,L=s.gql`
    query OrgConnectorSetup($orgSlug: String!) {
  currentUser {
    id
    __typename
    org(orgSlug: $orgSlug) {
      __typename
      ... on Org {
        id
        authorizations {
          editConnectorConfig(isCustomConfig: true) {
            isAuthorized
          }
        }
        connectors {
          ... on OrgConnectorConnection {
            items {
              ...OrgConnectorItem
            }
          }
        }
      }
      ... on NotFoundError {
        message
      }
    }
  }
}
    ${W}`;var H=e.i(366541);let Q={},K=s.gql`
    fragment SharedConnection on OrgConfiguredConnectorSharedConnection {
  connection {
    connectionId
    connectorName
  }
  groupScopes {
    ...OrgGroupsOrgGroup
  }
}
    ${z.OrgGroupsOrgGroupFragmentDoc}`,Y=s.gql`
    fragment ConfiguredConnectorItem on OrgConfiguredConnector {
  id
  connectorName
  displayName
  connectionCount
  config
  connector {
    ...OrgConnectorItem
  }
  sharedConnection {
    ...SharedConnection
  }
  repls {
    ...ConnectorContextReplInfo
  }
}
    ${W}
${K}
${H.ConnectorContextReplInfoFragmentDoc}`,J=s.gql`
    query ConfiguredConnectors($orgSlug: String!) {
  currentUser {
    id
    org(orgSlug: $orgSlug) {
      ... on Org {
        id
        dealContext {
          dealType
        }
        authorizations {
          editConnectorConfig(isCustomConfig: true) {
            isAuthorized
          }
        }
        configuredConnectors {
          ... on OrgConfiguredConnectorConnection {
            items {
              ...ConfiguredConnectorItem
            }
            pageInfo {
              hasNextPage
              hasPreviousPage
            }
          }
        }
      }
      ... on NotFoundError {
        message
      }
    }
  }
}
    ${Y}`,Z=s.gql`
    mutation DeleteConnectorConfig($input: DeleteConnectorConfigInput!) {
  deleteConnectorConfig(input: $input) {
    ... on Org {
      id
      configuredConnectors {
        ... on OrgConfiguredConnectorConnection {
          items {
            id
          }
        }
      }
    }
    ... on NotFoundError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    `,X=s.gql`
    mutation DeleteSharedOrgConnectionAndConfig($input: DeleteSharedOrgConnectionAndConfigInput!) {
  deleteSharedOrgConnectionAndConfig(input: $input) {
    ... on DeleteSharedOrgConnectionAndConfigResult {
      org {
        id
        configuredConnectors {
          ... on OrgConfiguredConnectorConnection {
            items {
              id
            }
          }
        }
      }
      deletedConnectionIds
    }
    ... on NotFoundError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    `;var ee=e.i(138716),en=e.i(829706),et=e.i(798060),eo=e.i(562782),er=e.i(927225),ea=e.i(674826),ei=e.i(859200),es=e.i(780902);let el={},ec=s.gql`
    mutation UpdateConnectorConfig($input: UpdateConnectorConfigInput!) {
  updateConnectorConfig(input: $input) {
    ... on Org {
      ... on Org {
        id
        configuredConnectors {
          ... on OrgConfiguredConnectorConnection {
            items {
              id
            }
          }
        }
      }
    }
    ... on UserError {
      message
    }
    ... on NotFoundError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    `;function ed(e){let n={...el,...e};return c.useMutation(ec,n)}let eu=s.gql`
    mutation createUpdateSharedOrgConnection($input: CreateUpdateSharedOrgConnectionInput!) {
  createUpdateSharedOrgConnection(input: $input) {
    ... on CreateUpdateSharedOrgConnectionResult {
      connectionId
      org {
        id
        connectors {
          ... on OrgConnectorConnection {
            items {
              ...OrgConnectorItem
            }
          }
        }
        configuredConnectors {
          ... on OrgConfiguredConnectorConnection {
            items {
              id
            }
          }
        }
        connectorContext {
          __typename
          ... on OrgConnectorContext {
            connectorConfigs {
              id
              webhookEvents {
                name
                model
                description
              }
            }
          }
          ... on Error {
            message
          }
        }
      }
    }
    ... on Error {
      message
    }
  }
}
    ${W}`;function eg(e){let n={...el,...e};return c.useMutation(eu,n)}let ep=s.gql`
    mutation UpdateOrgGroupSharedConnectionScopes($input: UpdateOrgGroupSharedConnectionScopesInput!) {
  updateOrgGroupSharedConnectionScopes(input: $input) {
    __typename
    ... on UpdateOrgGroupSharedConnectionScopesResult {
      connectionId
    }
    ... on UserError {
      message
    }
  }
}
    `,em=s.gql`
    query GetOrgConnectionKeys($input: GetConnectionKeysInput!) {
  getConnectionKeys(input: $input) {
    ... on ConnectionKeys {
      settings
    }
    ... on NotFoundError {
      message
    }
    ... on UnauthorizedError {
      message
    }
  }
}
    `;var eh=e.i(320216),eC=e.i(532764),ex=e.i(813707),ef=e.i(480028),e_=e.i(94824),ey=e.i(299560);let eS=({value:e,icon:t,title:o,description:r,selected:a})=>(0,n.jsxs)("label",{className:`${ey.default.optionCard} ${a?ey.default.selected:""}`,htmlFor:`radio-${e}`,children:[(0,n.jsx)(e_.Radio,{id:`radio-${e}`,value:e,className:ey.default.radioButton,checked:a}),(0,n.jsxs)(O.View,{className:ey.default.optionCardContent,children:[(0,n.jsxs)(O.View,{row:!0,gap:4,align:"center",children:[t,(0,n.jsx)(w.Text,{variant:"text",className:ey.default.title,children:o})]}),(0,n.jsx)(w.Text,{variant:"small",className:ey.default.description,children:r})]})]}),ej=({value:e="default",onChange:t,isDisabled:o=!1,isUpdate:r=!1})=>(0,n.jsxs)(O.View,{gap:8,children:[(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Text,{variant:"text",children:r?"Configurations":"Set up method"}),(0,n.jsx)(w.Text,{variant:"small",color:"dimmer",children:"Select how you'd like to configure your connector."})]}),(0,n.jsx)(e_.RadioGroup,{name:"setupMethod",value:e,onChange:t,children:(0,n.jsxs)(O.View,{className:ey.default.optionsContainer,children:[(0,n.jsx)(eS,{value:"default",icon:(0,n.jsx)(eC.default,{size:16,color:"default"===e?ef.tokens.accentPrimaryDefault:ef.tokens.foregroundDimmer}),title:"Use Replit default configurations",description:"Set up connector with Replit's default credentials.",selected:"default"===e}),o?(0,n.jsx)(w.Text,{variant:"small",color:"dimmer",children:"Upgrade to an Enterprise plan to use custom configurations."}):(0,n.jsx)(eS,{value:"custom",icon:(0,n.jsx)(ex.default,{size:16,color:"custom"===e?ef.tokens.accentPrimaryDefault:ef.tokens.foregroundDimmer}),title:"Use custom configurations",description:"Set up your own connector credentials and get fine tuned control.",selected:"custom"===e})]})})]});var ev=e.i(665271),ew=e.i(995446),eb=e.i(602686),eO=e.i(612343),eT=e.i(959787),eN=e.i(825419),eU=e.i(488299),eI=e.i(33583),eD=e.i(845415),eE=e.i(194751);function eA({group:e,onRemove:t}){let r=e.type===o.OrgGroupType.SystemIndividual&&e.individualMember?.email||e.name,a=t&&e.type!==o.OrgGroupType.SystemAdmins;return(0,n.jsxs)(O.View,{clsx:eE.default.groupBadge,row:!0,align:"center",gap:4,children:[e.type===o.OrgGroupType.SystemIndividual?(0,n.jsx)(eN.Avatar,{size:16,src:e.individualMember?.user?.image||null,username:e.individualMember?.user?.displayName||"",fullName:e.individualMember?.user?.fullName}):(0,n.jsx)(O.View,{p:4,clsx:eE.default.groupIcon,children:(0,n.jsx)(eO.default,{size:8})}),(0,n.jsx)(w.Text,{variant:"small",children:r}),a?(0,n.jsx)(eU.IconButton,{alt:"Remove group",tooltipBehavior:"hidden",onClick:()=>t(e.id),children:(0,n.jsx)(eb.default,{size:12})}):null]})}let eV=function({initialGroups:e,onGroupsChange:r,orgId:a}){let[i,s]=(0,t.useState)(e??[]),[l,c]=(0,t.useState)(""),d=[o.OrgGroupType.Custom,o.OrgGroupType.SystemIndividual,o.OrgGroupType.SystemMembers,o.OrgGroupType.SystemGuests],u=e=>{let n=i.filter(n=>n.id!==e);s(n),r&&r(n.map(e=>e.id))};return(0,n.jsxs)(O.View,{gap:16,children:[(0,n.jsxs)(eD.TextField,{children:[(0,n.jsx)(eI.Label,{variant:"text",children:"Access Controls"}),(0,n.jsx)(eD.TextFieldDescription,{children:"Manage which groups can use this connector. Admin groups always have access."}),(0,n.jsx)(eT.default,{inputId:"connector-group-search",orgId:a??"",types:d,selectedGroups:i,value:l,setValue:c,onSelect:e=>{if(i.some(n=>n.id===e.id))return;let n=[...i,e];s(n),c(""),r&&r(n.map(e=>e.id))},onClear:()=>{c("")},placeholder:"Search and select groups..."})]}),(0,n.jsx)(O.View,{gap:12,pb:12,children:(0,n.jsx)(O.View,{row:!0,gap:8,wrap:!0,children:i.length>0&&i.map(e=>(0,n.jsx)(eA,{group:e,onRemove:u},e.id))})})]})};var ek=e.i(643484),eF=e.i(903790),eM=e.i(190545),eR=e.i(180617),eB=e.i(610446);function eq({connector:e,onComplete:o,initialConfig:a,connectorConfigId:i,connectionSettings:s,sharedConnection:d,connectionCount:u=0,canUseCustomConfig:g=!1}){var p;let m,h,{name:C}=e??{},x=(0,R.useIsCurrentOrgEnterprise)(),f=(0,t.useMemo)(()=>({allowedScopes:e?.allowedScopes||[],defaultScopes:e?.defaultScopes||[]}),[e]),_=(0,t.useMemo)(()=>a?.oauth?.scopes&&a?.oauth?.scopes.length>0?a?.oauth?.scopes||[]:f.defaultScopes,[a,f]),[y,S]=(0,t.useState)(_),j=d?.__typename==="OrgConfiguredConnectorSharedConnection"&&d?.connection?.connectionId,v=j&&d?.groupScopes?d?.groupScopes:[],b=v.map(e=>e.id),[T,N]=(0,t.useState)("api_key"===e.type||!e.credentials||a&&a?.oauth&&a?.oauth?.client_id&&a?.oauth?.client_secret?"custom":"default"),[U,I]=(0,t.useState)(b),[D,E]=(0,t.useState)(!1),{showConfirm:A,showError:V}=(0,eh.default)(),{orgId:k,orgSlug:F}=(0,R.useCurrentUserStoredOrgContext)(),[M,{loading:B,error:q}]=ed({refetchQueries:[{query:r.OrgConnectorsPageDocument,variables:{orgSlug:F}}],onCompleted:e=>{"Org"===e.updateConnectorConfig.__typename?(A("Connector has been successfully updated"),o()):("UserError"===e.updateConnectorConfig.__typename||"UnauthorizedError"===e.updateConnectorConfig.__typename)&&V(e.updateConnectorConfig.message)},onError:()=>{V("Failed to update connector. Please try again.")}}),[G,{loading:$}]=eg({refetchQueries:[{query:r.OrgConnectorsPageDocument,variables:{orgSlug:F}},{query:J,variables:{orgSlug:F}},{query:L,variables:{orgSlug:F}},{query:em,variables:{input:{connectionId:d?.connection?.connectionId??"",connectorName:d?.connection?.connectorName,orgId:k}}}],onCompleted:e=>{"CreateUpdateSharedOrgConnectionResult"===e.createUpdateSharedOrgConnection.__typename?(A("Connector has been successfully updated"),o()):"UserError"===e.createUpdateSharedOrgConnection.__typename&&V(e.createUpdateSharedOrgConnection.message)},onError:()=>{V("Failed to create connection. Please try again.")}}),{data:z,loading:P}=(p={variables:{input:{connectionId:d?.connection?.connectionId??"",connectorName:d?.connection?.connectorName,orgId:k}},skip:!d?.connection?.connectionId||!d?.connection?.connectorName},m={...el,...p},l.useQuery(em,m)),[W,{loading:H}]=(h={...el,...void 0},c.useMutation(ep,h)),Q=(0,t.useMemo)(()=>"api_key"===e.type&&z?.getConnectionKeys?.__typename==="ConnectionKeys"?z.getConnectionKeys.settings:a||(e?.authType==="OAUTH2"?{oauth:{scopes:e.defaultScopes||[]}}:{}),[a,e,z]),K=e?.schemas?.connectorConfig,Y=async e=>{e.preventDefault(),C&&k&&await M({variables:{input:{connectorName:C,orgId:k,config:{oauth:{scopes:y}},connectorConfigId:i}},refetchQueries:[{query:J,variables:{orgSlug:F}},{query:r.OrgConnectorsPageDocument,variables:{orgSlug:F}},{query:L,variables:{orgSlug:F}},{query:em,variables:{input:{connectionId:d?.connection?.connectionId??"",connectorName:d?.connection?.connectorName,orgId:k}}}]})},Z=async e=>{C&&k&&await M({variables:{input:{connectorName:C,orgId:k,config:e,connectorConfigId:i}},refetchQueries:[{query:J,variables:{orgSlug:F}},{query:r.OrgConnectorsPageDocument,variables:{orgSlug:F}},{query:L,variables:{orgSlug:F}},{query:em,variables:{input:{connectionId:d?.connection?.connectionId??"",connectorName:d?.connection?.connectorName,orgId:k}}}]})},X=async e=>{if(C&&k&&(await G({variables:{input:{connectorName:C.toUpperCase().replace(/[-]/g,"_"),orgId:k,config:e}}}),x))try{await W({variables:{input:{connectorConfigId:i,groupIds:U,orgId:k}}})}catch(e){V("Connector updated successfully, but failed to update group permissions.")}},ee=B||$||H||!D||P,en="Update";return(0,n.jsx)(O.View,{gap:24,children:(0,n.jsx)(eM.Form,{onSubmit:"default"===T?Y:void 0,className:eB.default.form,children:(0,n.jsxs)(O.View,{gap:8,children:[q?(0,n.jsx)(ea.default,{children:q.message}):null,x&&j?(0,n.jsxs)(O.View,{children:[(0,n.jsx)(eV,{initialGroups:v,onGroupsChange:e=>{I(e),E(!0)},orgId:k}),(0,n.jsx)(eF.DividerH,{})]}):null,s&&"api_key"===e.type?(0,n.jsx)(ev.JSONSchemaForm,{jsonSchema:s,formContext:e,hideSubmitButton:!1,hideSensitiveFields:!1,onSubmit:X,disabled:ee,submitButtonText:en,formData:Q,onChange:()=>E(!0),disableScopes:u>0,loading:P}):(0,n.jsxs)(n.Fragment,{children:[e.credentials?(0,n.jsx)(ej,{value:T,onChange:e=>{let n=e.target.value;("default"===n||"custom"===n)&&(N(n),E(!0))},isDisabled:!g,isUpdate:!0}):null,"custom"===T?(0,n.jsxs)(O.View,{gap:16,children:[e.authType?.includes("OAUTH")?(0,n.jsx)(eR.default,{components:{p:e=>(0,n.jsx)(w.Text,{color:"dimmer",children:e.children})},clsx:eB.default.markdown,children:"In order to properly configure this connector, you need to set `https://replit.com/connectors/oauth/callback` as the Redirect URL in your app."}):null,(0,n.jsx)(ev.JSONSchemaForm,{jsonSchema:K,formData:Q,formContext:e,hideSubmitButton:!1,onSubmit:Z,disabled:ee,submitButtonText:en,onChange:()=>E(!0),disableScopes:u>0})]}):null]}),"default"===T&&(0,n.jsxs)(O.View,{gap:12,pt:12,children:[(0,n.jsx)(eF.DividerH,{className:eB.default.divider}),(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Text,{variant:"text",children:"Connector Scopes"}),(0,n.jsx)(w.Text,{variant:"small",color:"dimmer",children:"Connector scopes are permission mechanisms that define what specific resources and actions a connector is authorized to access on your account."})]}),(0,n.jsx)(ew.ScopesMultiSelect,{availableScopes:f.allowedScopes,selectedScopes:y,onChange:e=>{S(e),E(!0)},isDisabled:!g}),(0,n.jsx)(O.View,{pt:16,row:!0,justify:"end",children:(0,n.jsx)(ek.Button,{type:"submit",colorway:"primary",disabled:ee,loading:B||H,text:en})})]})]})})})}var eG=e.i(919073),e$=e.i(295231),ez=e.i(528326),eP=e.i(727223),eW=e.i(242001);let eL=({connector:e,onComplete:o,orgId:r,onClose:a})=>{var i,s;let l,d,[u,g]=(0,t.useState)(null),p=e.connector?.type==="api_key",[m,{loading:h}]=(i={onCompleted:e=>{e.deleteConnectorConfig?.__typename==="Org"?o():e.deleteConnectorConfig?.__typename==="NotFoundError"||e.deleteConnectorConfig?.__typename==="UnauthorizedError"?g(e.deleteConnectorConfig.message):g("An unexpected error occurred while deleting the connector.")},onError:()=>{g("Failed to delete connector. Please try again.")}},l={...Q,...i},c.useMutation(Z,l)),[C,{loading:x}]=(s={onCompleted:e=>{e.deleteSharedOrgConnectionAndConfig?.__typename==="DeleteSharedOrgConnectionAndConfigResult"?o():e.deleteSharedOrgConnectionAndConfig?.__typename==="NotFoundError"||e.deleteSharedOrgConnectionAndConfig?.__typename==="UnauthorizedError"?g(e.deleteSharedOrgConnectionAndConfig.message):g("An unexpected error occurred while deleting the connector and its connections.")},onError:()=>{g("Failed to delete connector and connections. Please try again.")}},d={...Q,...s},c.useMutation(X,d)),f=h||x;return(0,n.jsxs)(eG.ShadesSurface,{gap:24,p:12,clsx:eW.default.deleteCard,children:[(0,n.jsxs)(O.View,{gap:4,align:"start",children:[(0,n.jsxs)(w.Text,{variant:"subheadDefault",children:["Deleting ",e.connector?.displayName??e.connectorName," ","connector"]}),(0,n.jsx)(w.Text,{color:"dimmer",children:"Are you sure you want to delete this connector? This action cannot be undone and will remove the connector configuration from your workspace."})]}),u?(0,n.jsx)(ea.default,{children:u}):null,(0,n.jsxs)(O.View,{row:!0,gap:12,justify:"end",children:[(0,n.jsx)(ek.Button,{text:"Cancel",variant:"default",onClick:a,disabled:f}),(0,n.jsx)(ek.Button,{text:f?"Deleting...":"Delete connector",colorway:"negative",onClick:()=>{e.id?(g(null),p?C({variables:{input:{connectorConfigId:e.id,orgId:r}}}):m({variables:{input:{connectorConfigId:e.id,orgId:r}}})):g("Something went wrong. Please try again.")},loading:f,disabled:f})]})]})},eH=({connector:e,onClose:o,onDelete:r,onUpdate:a,orgId:i,canUseCustomConfig:s=!1})=>{let[l,c]=(0,t.useState)(!1),d=(0,es.useIsMobile)();if(!e?.connector||!e.id)return null;let u=Array.from(new Map((e.repls??[]).map(e=>[e.id,e])).values());return(0,n.jsx)(ez.Modal,{fromSide:!d,isOpen:!0,onRequestClose:()=>{c(!1),o()},hideCloseButton:!d,children:(0,n.jsxs)(O.View,{align:"start",clsx:eW.default.modal,children:[(0,n.jsx)(O.View,{pb:16,align:"start",children:e.connector.logoUrl?(0,n.jsx)(eG.ShadesSurface,{p:4,clsx:eW.default.imageContainer,children:(0,n.jsx)(eP.default,{width:36,height:36,src:e.connector.logoUrl,alt:e.displayName||e.connectorName})}):null}),(0,n.jsxs)(O.View,{justify:"space-between",row:!0,align:"center",clsx:eW.default.header,children:[(0,n.jsx)(w.Text,{variant:"headerDefault",multiline:!1,children:e.displayName||e.connector.displayName||e.connectorName}),(0,n.jsx)(e$.PopupMenu,{"aria-label":"Manage integration",trigger:(0,n.jsx)(eU.IconButton,{alt:"Manage integration",children:(0,n.jsx)(er.default,{})}),children:(0,n.jsx)(e$.MenuItem,{id:`delete-${e.id}`,label:"Delete",isDestructive:!0,onAction:()=>c(!0)})})]}),(0,n.jsx)(eF.DividerH,{clsx:eW.default.divider}),l?(0,n.jsx)(eL,{connector:e,onComplete:()=>{c(!1),r()},orgId:i,onClose:()=>c(!1)}):null,(0,n.jsxs)(O.View,{className:eW.default.tabsContainer,children:[(0,n.jsx)(O.View,{children:(0,n.jsx)(eq,{connector:e.connector,onComplete:a,initialConfig:e.config,connectorConfigId:e.id,connectionSettings:e.connector.schemas?.connectionSettings,sharedConnection:e.sharedConnection,connectionCount:e.connectionCount||0,canUseCustomConfig:s})}),(0,n.jsxs)(O.View,{className:eW.default.replSection,pt:8,gap:12,children:[(0,n.jsxs)(O.View,{pt:8,gap:4,children:[(0,n.jsx)(w.Text,{variant:"text",children:"Connected Apps"}),(0,n.jsx)(w.Text,{variant:"small",color:"dimmer",children:"Apps using this connector. Disconnecting may cause Apps to behave unexpectedly."})]}),(0,n.jsx)(ei.ConnectedAppsTable,{repls:u,emptyStateTitle:"No Apps connected",emptyStateDescription:"This connector hasn't been used by any Apps in your workspace yet."})]})]})]})})};var eQ=e.i(276887),eK=e.i(775007),eY=e.i(97043),eJ=e.i(68177);let eZ=({connector:e,onManage:t})=>(0,n.jsx)(O.View,{row:!0,justify:"end",children:e?(0,n.jsx)(ek.Button,{iconLeft:(0,n.jsx)(i.default,{}),variant:"default",text:"Manage",size:"small",onClick:()=>t(e)}):(0,n.jsx)(b.Tooltip,{tooltip:"Connector information is unavailable. This connector may have been removed or is temporarily unavailable.",placement:"left",children:(0,n.jsx)(ek.Button,{iconLeft:(0,n.jsx)(i.default,{}),variant:"default",text:"Manage",size:"small",disabled:!0})})}),eX=({orgSlug:e,onBack:o,setConnectorPageView:r,isAdmin:i})=>{var s;let c,[d,u]=(0,t.useState)(""),[g,p]=(0,t.useState)(null),m=(0,et.useOrgFlag)({controlName:"flag-self-hosted-git-domains"}),{data:h,loading:C,error:x}=(s={variables:{orgSlug:e},ssr:!1},c={...Q,...s},l.useQuery(J,c)),f=h?.currentUser?.__typename==="CurrentUser"&&h?.currentUser.org.__typename==="Org"?h.currentUser.org:null,y=f?.authorizations?.editConnectorConfig?.isAuthorized??!1,S=(0,eQ.isEnterpriseOrg)(f?.dealContext)&&m,T=(0,t.useMemo)(()=>{let e=f?.configuredConnectors?.__typename==="OrgConfiguredConnectorConnection"&&f.configuredConnectors.items||[];return S?e:e.filter(e=>!en.VERSION_CONTROL_CONNECTORS.has(e.connectorName))},[f,S]),N=(0,t.useMemo)(()=>new $.Fzf(T,{fuzzy:!1,selector:e=>`${e.displayName||e.connectorName} ${e.connector?.displayName||""}`}),[T]),U=(0,t.useMemo)(()=>d?N.find(d).map(e=>e.item):T,[N,d,T]),I=n=>{p(n),(0,B.track)(q.events.ORG_ADMIN_MANAGE_CONNECTOR_CLICKED,{connectorName:n.connectorName,orgSlug:e})};return x?(0,n.jsx)(O.View,{pt:16,children:(0,n.jsx)(w.Text,{color:"dimmer",children:"Error loading configured connectors"})}):(0,n.jsxs)(n.Fragment,{children:[(0,n.jsxs)(O.View,{gap:16,children:[(0,n.jsx)(O.View,{clsx:eJ.default.headerContainer,children:(0,n.jsxs)(O.View,{clsx:[eJ.default.searchBar,eJ.default.searchBarFull],row:!0,gap:8,children:[(0,n.jsx)(eY.SearchBar,{placeholder:"Search integrations",value:d,onChange:e=>u(e.target.value),onClear:()=>u("")}),(0,n.jsx)(b.Tooltip,{tooltip:"You must be an admin to enable new connectors",isDisabled:i,children:(0,n.jsx)(ek.Button,{text:"Add new connector",iconLeft:(0,n.jsx)(a.default,{}),onClick:()=>{(0,B.track)(q.events.ORG_VIEW_ENABLE_CONNECTORS_PAGE,{orgSlug:e}),r("setup")},disabled:!i,colorway:"primary"})})]})}),(0,n.jsx)(O.View,{row:!0,shrink:!0,pt:8,children:(0,n.jsx)(ek.Button,{size:"small",text:"Back",onClick:o,iconLeft:(0,n.jsx)(ee.default,{}),stretch:!1})}),(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Header,{level:2,variant:"subheadBig",children:"Manage Connectors"}),(0,n.jsx)(w.Text,{color:"dimmer",children:"Manage workspace-level connectors that have been configured for your team."})]}),(0,n.jsx)(O.View,{gap:16,children:(0,n.jsx)(_.IndexTable,{autoLayout:!0,title:"",columns:[{key:"name",label:"Name",isRowHeader:!0},{key:"connections",label:"Usage"},{key:"actions",label:""}],items:U,emptyState:(0,n.jsx)(eK.default,{title:"No connectors configured yet",description:"Configure your first connector to get started"}),loading:C,children:e=>(0,n.jsxs)(v.TableRow,{children:[(0,n.jsx)(j.TableCell,{children:(0,n.jsxs)(O.View,{gap:8,row:!0,align:"center",style:{minWidth:0,maxWidth:"90%"},children:[e.connector?.logoUrl?(0,n.jsx)(G.default,{width:24,height:24,src:e.connector.logoUrl,alt:`${e.displayName||e.connectorName} logo`,className:eJ.default.connectorIcon}):null,(0,n.jsx)(w.Text,{multiline:!1,children:e.connector?.displayName||e.connectorName})]})},"name"),(0,n.jsx)(j.TableCell,{children:(0,n.jsxs)(w.Text,{variant:"small",color:"dimmer",children:[e.connectionCount||0," ",(0,eo.default)("connection",e.connectionCount||0)]})},"connections"),(0,n.jsx)(j.TableCell,{children:(0,n.jsx)(eZ,{connector:e,onManage:I})},"actions")]},e.id)})})]}),f?(0,n.jsx)(eH,{connector:g,onClose:()=>p(null),onDelete:()=>p(null),onUpdate:()=>p(null),orgId:f.id,canUseCustomConfig:y}):null]})};var e0=e.i(416298),e1=e.i(723517);function e2({name:e,displayName:t,logoUrl:o,onClick:r,readonly:a}){let i=t||e;return(0,n.jsx)(b.Tooltip,{isDisabled:!a,tooltip:"Contact an admin to manage this connector",children:(0,n.jsx)(eG.ShadesSurface,{...a?{}:{css:e1.interactive.nofill},onClick:a?void 0:r,role:"button",tabIndex:0,style:{cursor:"pointer"},children:(0,n.jsxs)(O.View,{row:!0,gap:8,align:"center",p:8,children:[o?(0,n.jsx)(G.default,{src:o,alt:`${i} logo`,width:24,height:24,style:{objectFit:"contain",opacity:a?.75:1}}):null,(0,n.jsx)(w.Text,{color:a?"dimmer":"default",children:i})]})})})}var e4=e.i(534033);let e7={};function e8({connector:e,onComplete:o,connectionSettings:a,canUseCustomConfig:i=!1}){let{name:s,logoUrl:l}=e??{},c=e?.displayName||s,[d,u]=(0,t.useState)("api_key"!==e.type&&e.credentials?"default":"custom"),g=(0,t.useMemo)(()=>({allowedScopes:e?.allowedScopes||[],defaultScopes:e?.defaultScopes||[]}),[e]),[p,m]=(0,t.useState)(g.defaultScopes),{showConfirm:h,showError:C}=(0,eh.default)(),{orgId:x,orgSlug:f}=(0,R.useCurrentUserStoredOrgContext)(),[_,{loading:y,error:S}]=ed({refetchQueries:[{query:r.OrgConnectorsPageDocument,variables:{orgSlug:f}}],onCompleted:e=>{"Org"===e.updateConnectorConfig.__typename?(h("Connector has been successfully configured for your workspace"),o()):("UserError"===e.updateConnectorConfig.__typename||"UnauthorizedError"===e.updateConnectorConfig.__typename)&&C(e.updateConnectorConfig.message)},onError:()=>{C("Failed to enable connector. Please try again.")}}),[j,{loading:v}]=eg({refetchQueries:[{query:r.OrgConnectorsPageDocument,variables:{orgSlug:f}},{query:J,variables:{orgSlug:f}},{query:L,variables:{orgSlug:f}}],onCompleted:e=>{"CreateUpdateSharedOrgConnectionResult"===e.createUpdateSharedOrgConnection.__typename?(h("Connector has been successfully updated"),o()):C(e.createUpdateSharedOrgConnection.message)},onError:()=>{C("Failed to create connection. Please try again.")}}),b=e?.schemas?.connectorConfig,T=async e=>{e.preventDefault(),s&&x&&(await _({variables:{input:{connectorName:s,orgId:x,config:{oauth:{scopes:p}}}},refetchQueries:[{query:J,variables:{orgSlug:f}},{query:r.OrgConnectorsPageDocument,variables:{orgSlug:f}},{query:L,variables:{orgSlug:f}}]}),(0,B.track)(q.events.ORG_CREATE_CONNECTOR,{connectorName:s,orgSlug:f}))},N=async e=>{s&&x&&(await _({variables:{input:{connectorName:s,orgId:x,config:e}},refetchQueries:[{query:J,variables:{orgSlug:f}},{query:r.OrgConnectorsPageDocument,variables:{orgSlug:f}},{query:L,variables:{orgSlug:f}}]}),(0,B.track)(q.events.ORG_CREATE_CONNECTOR,{connectorName:s,orgSlug:f}))},U=async e=>{s&&x&&(await j({variables:{input:{connectorName:s.toUpperCase().replace(/[-]/g,"_"),orgId:x,config:e}}}),(0,B.track)(q.events.ORG_CREATE_CONNECTOR,{connectorName:s,orgSlug:f}))},I=y||v,D="Configure";return(0,n.jsxs)(O.View,{gap:24,children:[(0,n.jsxs)(O.View,{gap:16,align:"start",children:[l?(0,n.jsx)(eG.ShadesSurface,{p:4,align:"center",justify:"center",clsx:e4.default.logoContainer,children:(0,n.jsx)(G.default,{src:l,alt:`${c} logo`,width:32,height:32,style:{objectFit:"contain"}})}):null,(0,n.jsxs)(O.View,{gap:8,align:"start",children:[(0,n.jsxs)(w.Text,{variant:"headerDefault",children:["Enable ",c]}),(0,n.jsxs)(w.Text,{color:"dimmer",children:["Once configured, your entire workspace can use this ",c," ","connector to build Apps without needing their own API keys."]})]})]}),(0,n.jsx)(eM.Form,{onSubmit:"default"===d?T:void 0,className:e4.default.form,children:(0,n.jsxs)(O.View,{gap:8,children:[S?(0,n.jsx)(ea.default,{children:S.message}):null,a&&"api_key"===e.type?(0,n.jsx)(ev.JSONSchemaForm,{jsonSchema:a,formContext:e,hideSubmitButton:!1,hideSensitiveFields:!1,onSubmit:U,disabled:I,submitButtonText:D,formData:e7,disableScopes:!1,loading:!1}):(0,n.jsxs)(n.Fragment,{children:[e.credentials?(0,n.jsx)(ej,{value:d,onChange:e=>{let n=e.target.value;("default"===n||"custom"===n)&&u(n)},isDisabled:!i,isUpdate:!1}):null,"custom"===d&&b?(0,n.jsxs)(O.View,{gap:16,children:[e.authType?.includes("OAUTH")?(0,n.jsx)(eR.default,{components:{p:e=>(0,n.jsx)(w.Text,{color:"dimmer",children:e.children})},clsx:e4.default.markdown,children:"In order to properly configure this connector, you need to set `https://replit.com/connectors/oauth/callback` as the Redirect URL in your app."}):null,(0,n.jsx)(ev.JSONSchemaForm,{jsonSchema:b,formData:e7,formContext:e,hideSubmitButton:!1,onSubmit:N,disabled:I,submitButtonText:D,disableScopes:!1})]}):null]}),"default"===d&&(0,n.jsxs)(O.View,{gap:12,pt:12,children:[(0,n.jsx)(eF.DividerH,{className:e4.default.divider}),(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Text,{variant:"text",children:"Connector Scopes"}),(0,n.jsx)(w.Text,{variant:"small",color:"dimmer",children:"Connector scopes are permission mechanisms that define what specific resources and actions a connector is authorized to access on your account."})]}),(0,n.jsx)(ew.ScopesMultiSelect,{availableScopes:g.allowedScopes,selectedScopes:p,onChange:m,isDisabled:!i}),(0,n.jsx)(O.View,{pt:16,row:!0,justify:"end",children:(0,n.jsx)(ek.Button,{type:"submit",colorway:"primary",disabled:I,loading:y,text:D})})]})]})})]})}var e6=e.i(553780);function e5(){return(0,n.jsx)(eG.ShadesSurface,{children:(0,n.jsx)(O.View,{row:!0,gap:8,align:"center",p:8,children:(0,n.jsx)(O.View,{className:`${e6.default.loadingSkeleton} ${e6.default.loadingText}`})})})}function e9({orgSlug:e,onBack:o,isAdmin:r=!1}){var a;let i,s=(0,es.useIsMobile)(),[c,d]=(0,t.useState)(null),[u,g]=(0,t.useState)(""),{data:p,loading:m,error:h}=(a={variables:{orgSlug:e},ssr:!1},i={...P,...a},l.useQuery(L,i)),C=()=>{d(null)},x=p?.currentUser?.__typename==="CurrentUser"&&p?.currentUser.org?.__typename==="Org"?p.currentUser.org:null,f=x?.authorizations?.editConnectorConfig?.isAuthorized??!1,_=(0,t.useMemo)(()=>x&&x.connectors&&"OrgConnectorConnection"===x.connectors.__typename?(x.connectors.items??[]).filter(e=>"stripe"!==e.name.toLowerCase()):[],[x]),S=(0,t.useMemo)(()=>new $.Fzf(_,{fuzzy:!1,selector:e=>`${e.name} ${e.displayName??""}`}),[_]),j=(0,t.useMemo)(()=>u?S.find(u).map(e=>e.item):_,[S,u,_]);return h?(0,n.jsx)(O.View,{children:(0,n.jsx)(w.Text,{children:"Error loading connectors"})}):(0,n.jsxs)(O.View,{gap:16,children:[(0,n.jsx)(O.View,{clsx:e6.default.headerContainer,children:(0,n.jsx)(O.View,{clsx:[e6.default.searchBar,e6.default.searchBarFull],children:(0,n.jsx)(eY.SearchBar,{placeholder:"Search integrations",value:u,onChange:e=>g(e.target.value),onClear:()=>g("")})})}),o?(0,n.jsx)(O.View,{row:!0,shrink:!0,pt:8,children:(0,n.jsx)(ek.Button,{size:"small",text:"Back",onClick:o,iconLeft:(0,n.jsx)(ee.default,{}),stretch:!1})}):null,(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Header,{level:2,variant:"subheadBig",children:r?"Enable a connector":"Available connectors"}),(0,n.jsx)(w.Text,{color:"dimmer",children:"Connectors are shared integrations that your entire team can use to build apps. Set up once, and everyone can access the same database, API, or service without managing individual credentials."}),r||m?null:(0,n.jsx)(O.View,{pt:8,children:(0,n.jsx)(y.StatusBanner,{colorway:"warning",icon:(0,n.jsx)(e0.default,{}),text:"Contact an admin to enable new connectors."})})]}),(0,n.jsxs)(O.View,{gap:16,className:e6.default.connectorSetup,children:[(0,n.jsx)(O.View,{className:e6.default.connectorGrid,children:m?Array.from({length:12},(e,t)=>(0,n.jsx)(e5,{},`loading-${t}`)):(0,n.jsx)(n.Fragment,{children:j.map(t=>(0,n.jsx)(eG.ShadesSurface,{className:e6.default.cardContainer,elevate:"2x",children:(0,n.jsx)(e2,{name:t.name,displayName:t.displayName,logoUrl:t.logoUrl,onClick:()=>{(0,B.track)(q.events.ORG_CONNECTOR_SETUP_STARTED,{connectorName:t.name,orgSlug:e}),d(t)},readonly:!r})},t.name))})}),m||0!==j.length?null:(0,n.jsx)(O.View,{className:e6.default.emptyState,p:32,children:(0,n.jsx)(w.Text,{color:"dimmer",children:u.trim()?`No connectors found matching "${u}"`:"No connectors available"})})]}),(0,n.jsx)(ez.Modal,{fromSide:!s,isOpen:!!c,hideCloseButton:!s,onRequestClose:C,children:c?(0,n.jsx)(O.View,{className:e6.default.modal,children:(0,n.jsx)(e8,{connector:c,onComplete:()=>{C(),o?.()},connectionSettings:c.schemas?.connectionSettings,canUseCustomConfig:f})}):null})]})}var e3=e.i(953956);let ne=({orgSlug:e})=>{let{orgId:s,orgRole:l}=(0,R.useCurrentUserStoredOrgContext)(),c=l===o.SystemOrgGroupType.SystemAdmins,{data:d,loading:u,error:g,refetch:p}=(0,r.useOrgConnectorsPageQuery)({variables:{orgSlug:e},ssr:!1}),[m]=(0,r.useCreateOrgConnectionMutation)(),[h]=(0,r.useDeleteOrgConnectionMutation)(),[C,x]=(0,t.useState)("list"),[f,_]=(0,t.useState)(""),y=(0,t.useCallback)(async n=>{s&&await h({variables:{input:{connectionId:n,orgId:s}},optimisticResponse:{__typename:"RootMutationType",deleteConnection:{__typename:"DeleteConnection",success:!0}},update(t){try{let o=t.readQuery({query:r.OrgConnectorsPageDocument,variables:{orgSlug:e}});if(o?.currentUser?.__typename==="CurrentUser"&&o.currentUser.org?.__typename==="Org"){let a=o.currentUser.org.connectorContext.connections.filter(e=>e.connectionId!==n);t.writeQuery({query:r.OrgConnectorsPageDocument,variables:{orgSlug:e},data:{currentUser:{...o.currentUser,org:{...o.currentUser.org,connectorContext:{...o.currentUser.org.connectorContext,connections:a}}}}})}}catch{}}})},[h,s,e]),S=async e=>{s&&"connect.connection-connected"===e.name&&(await m({variables:{input:{connectionId:e.data.connection_id,orgId:s??""}}}),await p())},j=d?.currentUser?.__typename==="CurrentUser"&&d?.currentUser.org.__typename==="Org"?d?.currentUser?.org?.connectorContext:null,v=null,T=[],N=[],U=[];if(j?.__typename==="OrgConnectorContext"&&(v=j.openIntClientToken,T=j.connections??[],N=j.connectorConfigs??[],U=j.connectorWhitelist??[]),g)return(0,n.jsx)(O.View,{children:(0,n.jsx)(w.Text,{children:"Error loading connectors"})});let I=0===N.length&&0===T.length;return"setup"===C||I?(0,n.jsxs)(O.View,{gap:48,children:[(0,n.jsx)(e9,{orgSlug:e,onBack:I?void 0:()=>x("list"),isAdmin:c}),s?(0,n.jsx)(A,{orgId:s}):null,(0,n.jsx)(F.McpServersSection,{query:f}),(0,n.jsx)(k.GitProvidersSection,{query:f})]}):"manage"===C?(0,n.jsx)(O.View,{children:(0,n.jsx)(eX,{orgSlug:e,onBack:()=>x("list"),setConnectorPageView:x,isAdmin:c})}):(0,n.jsxs)(O.View,{gap:48,children:[(0,n.jsx)(O.View,{clsx:e3.default.headerContainer,align:"start",gap:16,children:(0,n.jsxs)(O.View,{row:!0,gap:8,clsx:[e3.default.searchControls,e3.default.searchControlsFull],children:[(0,n.jsx)(eY.SearchBar,{placeholder:"Search integrations",value:f,onChange:e=>_(e.target.value),onClear:()=>_("")}),c?(0,n.jsx)(ek.Button,{text:"Manage connectors",iconLeft:(0,n.jsx)(i.default,{}),onClick:()=>{x("manage")},variant:"outlined"}):null,(0,n.jsx)(b.Tooltip,{tooltip:"You must be an admin to enable new connectors",isDisabled:c,children:(0,n.jsx)(ek.Button,{text:"Add new connector",iconLeft:(0,n.jsx)(a.default,{}),onClick:()=>{(0,B.track)(q.events.ORG_VIEW_ENABLE_CONNECTORS_PAGE,{orgSlug:e}),x("setup")},disabled:!c,colorway:"primary"})})]})}),(0,n.jsxs)(O.View,{gap:16,children:[(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Header,{level:2,variant:"subheadBig",children:"Replit managed"}),(0,n.jsx)(w.Text,{color:"dimmer",children:"These are built-in integrations that work automatically. Create an app and your agent can start using these right away."})]}),(0,n.jsx)(M.ReplitManagedTable,{query:f})]}),(0,n.jsxs)(O.View,{gap:16,children:[(0,n.jsxs)(O.View,{gap:4,children:[(0,n.jsx)(w.Header,{level:2,variant:"subheadBig",children:"Connectors"}),(0,n.jsx)(w.Text,{color:"dimmer",children:"These are first-party integrations Replit supports. Sign in once and build with them across your apps."})]}),(0,n.jsx)(V.ConnectorsShared,{token:v??"",connections:T,connectorConfigs:N,onDelete:y,onEvent:S,query:f,shouldShowConnectButton:!1,whitelist:U,isLoading:u})]}),s?(0,n.jsx)(A,{orgId:s}):null,(0,n.jsx)(F.McpServersSection,{query:f}),(0,n.jsx)(k.GitProvidersSection,{query:f})]})};e.s(["OrgConnectors",0,ne,"default",0,ne],28733)}]);

//# debugId=3cfc77e5-ca70-08c1-17b4-3ac26a1d222d
//# sourceMappingURL=0jjrzagqv5rrc.js.map
